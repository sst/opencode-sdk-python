#!/usr/bin/env python
"""Reusable generator for discriminated-union variant models.

Given the path to the OpenAPI spec and the name of a top-level ``anyOf`` union
schema (e.g. ``Part``, ``Event``), this script resolves every variant in the
union, converts each variant's JSON Schema object into a pydantic ``BaseModel``
subclass (including any nested anonymous sub-objects), and prints the full
Python module *body* to stdout -- imports, ``__all__``, every variant class
(and its nested classes), and finally the ``Union[...]`` discriminated
``TypeAlias``.

It intentionally does NOT write any files itself; the caller pipes stdout into
the target module (e.g. ``src/opencode_ai/types/part.py``) and hand-edits the
header/glue as needed. This keeps the generator dumb, deterministic, and easy
to diff.

Usage:

    ./.venv/Scripts/python.exe scripts/gen_union_models.py --union Part > /tmp/part_body.py
    ./.venv/Scripts/python.exe scripts/gen_union_models.py --union Event --unknown-fallback EventUnknown

Design notes (why it looks the way it does):

* Every variant in the union is required to be a ``$ref`` to a named
  ``components/schemas`` entry whose own schema is a plain ``object`` with a
  single-value ``enum`` (or ``const``) on a ``type`` property -- exactly the
  discriminated-union convention this SDK follows everywhere else.
* Nested anonymous objects (``{"type": "object", "properties": {...}}`` with
  no ``$ref``) are recursively turned into their own nested classes named
  ``<ParentClass><PropertyNameInPascalCase>``, so two variants can each have a
  field called e.g. ``time`` without colliding in the shared module namespace.
* Nested ``$ref``s are handled two ways, controlled by ``KNOWN_MODULES``:
    1. "whole reuse" -- the ref name itself has a dedicated existing module
       (e.g. ``FilePartSource`` -> ``file_part_source.py``). We just import
       the name directly and use it as the field's type.
    2. "member reuse" -- the ref points to an *anonymous* union schema (its
       own ``anyOf``) whose *members* each have dedicated modules (e.g.
       ``ToolState`` is unioning ``ToolStatePending``/``ToolStateRunning``/
       ``ToolStateCompleted``/``ToolStateError``, none of which is named
       ``ToolState`` itself). We import each member and synthesize a local
       ``<ParentClass><PropertyName>: TypeAlias = Annotated[Union[...],
       PropertyInfo(discriminator=...)]`` right there in the module, mirroring
       how ``tool_part.py`` already hand-rolls its local ``State`` alias.
  Any ``$ref`` that is neither is inlined as if it were an anonymous object
  (best-effort fallback for schemas the registry doesn't know about yet).
* Field ordering follows the convention already established by every
  hand-written model in this repo: ``id`` first (if present), then
  the rest of the *required* fields alphabetically by their Python
  (snake_case) name, then a blank line, then the *optional* fields
  alphabetically.
"""

from __future__ import annotations

import re
import json
import keyword
import argparse
from typing import Any, Set, Dict, List, Tuple, Optional

# ---------------------------------------------------------------------------
# Registry of schema names that already have a dedicated module elsewhere in
# `opencode_ai.types` and should be imported rather than re-generated inline.
#
# Maps schema name -> dotted module path, relative to `opencode_ai.types`.
# ---------------------------------------------------------------------------
KNOWN_MODULES: Dict[str, str] = {
    "FilePartSource": "file_part_source",
    "APIError": "shared.api_error",
    "ToolStatePending": "tool_state_pending",
    "ToolStateRunning": "tool_state_running",
    "ToolStateCompleted": "tool_state_completed",
    "ToolStateError": "tool_state_error",
    "UnknownError": "shared.unknown_error",
    "ProviderAuthError": "shared.provider_auth_error",
    "MessageAbortedError": "shared.message_aborted_error",
    "ContextOverflowError": "shared.context_overflow_error",
    "StructuredOutputError": "shared.structured_output_error",
    "Message": "message",
    "Session": "session",
    "Part": "part",
}


def camel_to_snake(name: str) -> str:
    s1 = re.sub(r"(.)([A-Z][a-z]+)", r"\1_\2", name)
    s2 = re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", s1)
    return s2.lower()


def literal_type(enum_values: List[Any]) -> str:
    """Render a JSON Schema `enum` (of any length -- single-value discriminator
    consts and multi-value string enums alike, e.g. `["rename", "change"]`) as
    a Python `Literal[...]`."""
    values = ", ".join(f'"{v}"' if isinstance(v, str) else repr(v) for v in enum_values)
    return f"Literal[{values}]"


def safe_field_name(snake_name: str) -> str:
    """Append a trailing underscore to Python-keyword field names (e.g. the
    literal wire property ``from`` on ``EventAccountSwitchedProperties``) so
    the generated attribute is a valid identifier. The original wire name is
    preserved separately and always carried through as the pydantic alias."""
    return f"{snake_name}_" if keyword.iskeyword(snake_name) else snake_name


def snake_to_pascal(snake_name: str) -> str:
    return "".join(part[:1].upper() + part[1:] for part in snake_name.split("_") if part)


def sanitize_class_name(name: str) -> str:
    """Best-effort PascalCase sanitizer for schema names that aren't already clean."""
    if re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", name):
        return name
    parts = re.split(r"[^A-Za-z0-9]+", name)
    return "".join(p[:1].upper() + p[1:] for p in parts if p)


class Field:
    def __init__(self, prop_name: str, snake_name: str, required: bool, type_str: str, is_literal_type: bool = False):
        self.prop_name = prop_name
        self.snake_name = snake_name
        self.required = required
        self.type_str = type_str
        self.is_literal_type = is_literal_type

    @property
    def alias(self) -> Optional[str]:
        return self.prop_name if self.prop_name != self.snake_name else None

    def render(self) -> str:
        if self.required:
            if self.alias:
                return f'    {self.snake_name}: {self.type_str} = FieldInfo(alias="{self.alias}")'
            return f"    {self.snake_name}: {self.type_str}"
        else:
            optional_type = self.type_str if self.type_str.startswith("Optional[") else f"Optional[{self.type_str}]"
            if self.alias:
                return f'    {self.snake_name}: {optional_type} = FieldInfo(alias="{self.alias}", default=None)'
            return f"    {self.snake_name}: {optional_type} = None"


class Generator:
    def __init__(self, spec: Dict[str, Any]):
        self.schemas: Dict[str, Any] = spec["components"]["schemas"]
        self.nested_classes: List[str] = []  # rendered class source blocks, in emission order
        self.imports: Dict[str, Set[str]] = {}  # module -> set(names)
        self.all_names: List[str] = []

    # -- import bookkeeping ------------------------------------------------
    def _add_import(self, module: str, name: str) -> None:
        self.imports.setdefault(module, set()).add(name)

    # -- ref resolution ------------------------------------------------
    def _ref_name(self, ref: str) -> str:
        return ref.rsplit("/", 1)[-1]

    def _find_discriminator_field(self, member_schemas: List[Dict[str, Any]]) -> str:
        """Best-effort: find a required property present on every member whose
        value is a single-value enum -- the classic discriminator shape."""
        candidates: Optional[Set[str]] = None
        for member in member_schemas:
            required = set(member.get("required", []))
            single_enum_props = {
                pname
                for pname, pschema in member.get("properties", {}).items()
                if pname in required and len(pschema.get("enum", []) or []) == 1
            }
            candidates = single_enum_props if candidates is None else (candidates & single_enum_props)
        if candidates:
            return sorted(candidates)[0]
        return "type"

    # -- type resolution ------------------------------------------------
    def _resolve_type(
        self,
        prop_schema: Dict[str, Any],
        *,
        parent_class: str,
        prop_name: str,
    ) -> str:
        prop_snake = camel_to_snake(prop_name)
        nested_class_name = parent_class + snake_to_pascal(prop_snake)

        if "$ref" in prop_schema:
            ref_name = self._ref_name(prop_schema["$ref"])
            return self._resolve_ref(ref_name, nested_class_name)

        if "anyOf" in prop_schema:
            class_name = parent_class + snake_to_pascal(prop_snake)
            return self._resolve_anyof(prop_schema["anyOf"], class_name=class_name)

        json_type = prop_schema.get("type")

        if json_type == "object":
            props = prop_schema.get("properties")
            if not props:
                return "object"
            return self._emit_object_class(nested_class_name, prop_schema)

        if json_type == "array":
            items = prop_schema.get("items", {})
            item_type = self._resolve_type(items, parent_class=parent_class, prop_name=prop_name)
            return f"List[{item_type}]"

        if json_type == "string":
            if prop_schema.get("enum"):
                return literal_type(prop_schema["enum"])
            return "str"
        if json_type == "integer":
            return "int"
        if json_type == "number":
            return "float"
        if json_type == "boolean":
            return "bool"

        # Unknown / unspecified JSON schema shape -- safest permissive fallback.
        return "object"

    def _resolve_ref(self, ref_name: str, nested_class_name: str) -> str:
        if ref_name in KNOWN_MODULES:
            self._add_import(KNOWN_MODULES[ref_name], ref_name)
            return ref_name

        ref_schema = self.schemas.get(ref_name, {})
        if not ref_schema:
            return "object"

        if "anyOf" in ref_schema:
            members = ref_schema["anyOf"]
            member_refs = [m["$ref"] for m in members if "$ref" in m]
            if len(member_refs) == len(members) and all(self._ref_name(r) in KNOWN_MODULES for r in member_refs):
                member_names = [self._ref_name(r) for r in member_refs]
                member_schemas = [self.schemas[m] for m in member_names]
                for m in member_names:
                    self._add_import(KNOWN_MODULES[m], m)
                discriminator = self._find_discriminator_field(member_schemas)
                union_members = ", ".join(member_names)
                alias_src = (
                    f"{nested_class_name}: TypeAlias = Annotated[\n"
                    f'    Union[{union_members}], PropertyInfo(discriminator="{discriminator}")\n'
                    f"]"
                )
                self.nested_classes.append(alias_src)
                self.all_names.append(nested_class_name)
                return nested_class_name
            # Not every member has a dedicated module -- synthesize a locally
            # scoped discriminated union, inlining whichever members lack one.
            return self._resolve_anyof(members, class_name=nested_class_name)

        # A named ref that isn't an `anyOf` can still be shaped like anything a
        # regular property can be (a plain object, an array, or even a bare
        # scalar) -- dispatch on its JSON type the same way `_resolve_type`
        # does for inline schemas, just naming any emitted class after the
        # *property* that pointed here rather than the ref's own (possibly
        # non-identifier) schema name.
        json_type = ref_schema.get("type")
        if json_type == "array":
            item_type = self._resolve_type(
                ref_schema.get("items", {}), parent_class=nested_class_name, prop_name="item"
            )
            return f"List[{item_type}]"
        if json_type == "string":
            if ref_schema.get("enum"):
                return literal_type(ref_schema["enum"])
            return "str"
        if json_type == "integer":
            return "int"
        if json_type == "number":
            return "float"
        if json_type == "boolean":
            return "bool"
        if ref_schema.get("properties"):
            return self._emit_object_class(nested_class_name, ref_schema)

        # Unknown/unspecified/empty-object shape -- safest permissive fallback.
        return "object"

    def _resolve_anyof(
        self,
        members: List[Dict[str, Any]],
        *,
        class_name: str,
    ) -> str:
        """Handle an inline (unnamed) ``anyOf`` on a property -- as distinct from
        ``_resolve_ref``, which handles a ``$ref`` that itself points at a named
        ``anyOf`` schema. Two shapes are supported:

        1. A union of plain strings (e.g. a string enum plus an unconstrained
           ``string`` alternative) -- collapses to ``str``, since the enum'd
           members are always a strict subset of the unconstrained alternative.
        2. A discriminated union of objects, where each member is either a
           ``$ref`` (reused via ``KNOWN_MODULES`` if registered, else inlined as
           a locally-scoped nested class) or an inline object schema (always
           inlined). A local ``Union[...]`` discriminator alias is synthesized,
           named ``<ParentClass><PropertyNameInPascalCase>``.
        """
        if all(m.get("type") == "string" for m in members) and not any("$ref" in m for m in members):
            return "str"

        union_names: List[str] = []
        member_schemas: List[Dict[str, Any]] = []
        for idx, member in enumerate(members):
            if "$ref" in member:
                ref_name = self._ref_name(member["$ref"])
                ref_schema = self.schemas.get(ref_name, {})
                if ref_name in KNOWN_MODULES:
                    self._add_import(KNOWN_MODULES[ref_name], ref_name)
                    union_names.append(ref_name)
                else:
                    cls_name = class_name + sanitize_class_name(ref_name)
                    union_names.append(self._emit_object_class(cls_name, ref_schema))
                member_schemas.append(ref_schema)
            elif member.get("type") == "object":
                type_prop = member.get("properties", {}).get("type", {})
                enum_vals: List[Any] = type_prop.get("enum") or []
                suffix = snake_to_pascal(camel_to_snake(str(enum_vals[0]))) if enum_vals else str(idx)
                union_names.append(self._emit_object_class(class_name + suffix, member))
                member_schemas.append(member)
            # else: non-object, non-ref member mixed into an otherwise object-ish
            # union -- best-effort: dropped, since it can't be modeled as a class.

        if not union_names:
            return "object"
        if len(union_names) == 1:
            return union_names[0]

        discriminator = self._find_discriminator_field(member_schemas)
        union_members = ", ".join(union_names)
        alias_src = (
            f"{class_name}: TypeAlias = Annotated[\n"
            f'    Union[{union_members}], PropertyInfo(discriminator="{discriminator}")\n'
            f"]"
        )
        self.nested_classes.append(alias_src)
        self.all_names.append(class_name)
        return class_name

    def _emit_object_class(self, class_name: str, schema: Dict[str, Any]) -> str:
        fields = self._build_fields(class_name, schema)
        body_lines: List[str] = []
        required_fields = [f for f in fields if f.required]
        optional_fields = [f for f in fields if not f.required]
        for f in required_fields:
            body_lines.append(f.render())
            body_lines.append("")
        if optional_fields:
            for f in optional_fields:
                body_lines.append(f.render())
                body_lines.append("")
        if body_lines and body_lines[-1] == "":
            body_lines.pop()
        if not body_lines:
            body_lines = ["    pass"]
        src = f"class {class_name}(BaseModel):\n" + "\n".join(body_lines)
        self.nested_classes.append(src)
        self.all_names.append(class_name)
        return class_name

    def _build_fields(self, parent_class: str, schema: Dict[str, Any]) -> List[Field]:
        properties: Dict[str, Any] = schema.get("properties", {})
        required = set(schema.get("required", []))

        entries: List[Tuple[str, str, bool, Dict[str, Any]]] = []
        for prop_name, prop_schema in properties.items():
            snake_name = safe_field_name(camel_to_snake(prop_name))
            entries.append((prop_name, snake_name, prop_name in required, prop_schema))

        def sort_key(entry: Tuple[str, str, bool, Dict[str, Any]]) -> Tuple[int, str]:
            _, snake_name, is_required, _ = entry
            if snake_name == "id":
                return (0, snake_name)
            return (1 if is_required else 2, snake_name)

        entries.sort(key=sort_key)

        fields: List[Field] = []
        for prop_name, snake_name, is_required, prop_schema in entries:
            # Any enum -- single-value discriminator consts (`type`/`name` fields)
            # as well as ordinary multi-value string enums (e.g. `event: "rename"
            # | "change"`) -- renders as a Literal, never a bare `str`.
            if "enum" in prop_schema and prop_schema["enum"]:
                type_str = literal_type(prop_schema["enum"])
                fields.append(Field(prop_name, snake_name, is_required, type_str, is_literal_type=True))
                continue
            type_str = self._resolve_type(prop_schema, parent_class=parent_class, prop_name=prop_name)
            fields.append(Field(prop_name, snake_name, is_required, type_str))
        return fields

    # -- variant / union emission ------------------------------------------------
    def emit_variant(self, schema_name: str) -> str:
        class_name = sanitize_class_name(schema_name)
        schema = self.schemas[schema_name]
        return self._emit_object_class(class_name, schema)

    def generate(self, union_name: str, unknown_fallback: Optional[str]) -> str:
        union_schema = self.schemas[union_name]
        variant_refs = [self._ref_name(m["$ref"]) for m in union_schema["anyOf"] if "$ref" in m]

        variant_class_names: List[str] = []
        for ref_name in variant_refs:
            class_name = self.emit_variant(ref_name)
            variant_class_names.append(class_name)

        lines: List[str] = []

        # imports
        lines.append("from typing import List, Union, Optional")
        lines.append("from typing_extensions import Literal, Annotated, TypeAlias")
        lines.append("")
        lines.append("from pydantic import Field as FieldInfo")
        lines.append("")
        lines.append("from .._utils import PropertyInfo")
        lines.append("from .._models import BaseModel")
        for module in sorted(self.imports):
            names = ", ".join(sorted(self.imports[module]))
            dotted = "." + module
            lines.append(f"from {dotted} import {names}")
        lines.append("")

        all_entries = [union_name]
        if unknown_fallback:
            all_entries.append(unknown_fallback)
        all_entries.extend(self.all_names)
        all_literal = ", ".join(f'"{n}"' for n in all_entries)
        lines.append(f"__all__ = [{all_literal}]")
        lines.append("")
        lines.append("")

        for src in self.nested_classes:
            lines.append(src)
            lines.append("")
            lines.append("")

        if unknown_fallback:
            lines.append(f"class {unknown_fallback}(BaseModel):")
            lines.append(
                f'    """Permissive fallback for `{union_name}` `type` values not yet enumerated by this SDK."""'
            )
            lines.append("")
            lines.append("    type: str")
            lines.append("")
            lines.append("")

        union_members = ", ".join(([unknown_fallback] if unknown_fallback else []) + variant_class_names)
        lines.append(f"{union_name}: TypeAlias = Annotated[")
        lines.append(f"    Union[{union_members}],")
        lines.append('    PropertyInfo(discriminator="type"),')
        lines.append("]")

        return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--spec",
        default="../opencode-openapi-spec.json",
        help="Path to the OpenAPI spec JSON (relative to the repo root)",
    )
    parser.add_argument("--union", required=True, help="Name of the top-level anyOf union schema, e.g. Part")
    parser.add_argument(
        "--unknown-fallback",
        default=None,
        help="If set, emit a permissive fallback class with this name as the first union member",
    )
    args = parser.parse_args()

    with open(args.spec, encoding="utf-8") as f:
        spec = json.load(f)

    gen = Generator(spec)
    print(gen.generate(args.union, args.unknown_fallback))


if __name__ == "__main__":
    main()
