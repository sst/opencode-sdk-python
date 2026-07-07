#!/usr/bin/env python
"""Generate an all-fields example-JSON reference for the SDK's response types.

For every top-level type listed in api.md, this constructs an example value
with *every* field populated (required and optional), in wire shape (by alias),
so you can see at a glance which fields a payload can carry. Discriminated
unions (Part, EventListResponse, ...) are expanded: each variant gets its own
example, so e.g. `EventMessagePartUpdated` shows up under Event.

Values are type-indicating placeholders ("string", 0, false, the literal value
for Literal fields), not real data -- the point is the shape, not sample content.

Output: docs/type-examples.md (grouped by resource, one ```json block per type).

Regenerate with:
    ./.venv/Scripts/python.exe scripts/gen_type_examples.py
"""

from __future__ import annotations

import re
import enum
import json
import typing
import datetime
import typing_extensions as tpx
from typing import Any, Dict, List, Tuple, Optional, cast
from pathlib import Path

import opencode_ai.types as types_mod
from opencode_ai._models import BaseModel

# typing_extensions.get_origin/get_args normalize constructs (Literal, Annotated,
# Required/NotRequired) built from typing_extensions, which on Python 3.9 are not
# identical to their typing counterparts.
LITERAL_ORIGINS = {typing.Literal, tpx.Literal}
UNION_ORIGINS = {typing.Union}
REQUIRED_ORIGINS = {tpx.Required, tpx.NotRequired}

REPO_ROOT = Path(__file__).resolve().parent.parent
API_MD = REPO_ROOT / "api.md"
OUT_MD = REPO_ROOT / "docs" / "type-examples.md"
OUT_JSON = REPO_ROOT / "docs" / "type-examples.json"

MAX_DEPTH = 10


def unwrap_annotated(tp: Any) -> Tuple[Any, Tuple[Any, ...]]:
    """Return (real_type, metadata) for Annotated[...], else (tp, ())."""
    if hasattr(tp, "__metadata__"):
        return tp.__origin__, tp.__metadata__
    return tp, ()


def is_typeddict(tp: Any) -> bool:
    return hasattr(tp, "__required_keys__") and hasattr(tp, "__annotations__")


def is_model(tp: Any) -> bool:
    return isinstance(tp, type) and issubclass(tp, BaseModel)


def alias_from_metadata(metadata: Tuple[Any, ...]) -> Optional[str]:
    for m in metadata:
        alias = getattr(m, "alias", None)
        if isinstance(alias, str):
            return alias
    return None


def pick_union_member(members: List[Any]) -> Any:
    """Choose a representative union member: first non-Unknown model, else first."""
    models = [m for m in members if is_model(m)]
    for m in models:
        if not m.__name__.endswith("Unknown"):
            return m
    if models:
        return models[0]
    return members[0]


def example_for(tp: Any, seen: frozenset[str], depth: int) -> Any:
    tp, _meta = unwrap_annotated(tp)

    if depth > MAX_DEPTH:
        return "..."

    origin = tpx.get_origin(tp)
    args = tpx.get_args(tp)

    if origin in REQUIRED_ORIGINS:
        return example_for(args[0], seen, depth) if args else {}

    if origin in LITERAL_ORIGINS:
        return args[0] if args else "..."

    if origin in UNION_ORIGINS:
        non_none = [a for a in args if a is not type(None)]
        if not non_none:
            return None
        return example_for(pick_union_member(non_none), seen, depth)

    if origin in (list, set, frozenset, tuple):
        inner = args[0] if args else str
        return [example_for(inner, seen, depth + 1)]

    if origin in (dict,) or tp is dict:
        val = args[1] if len(args) > 1 else str
        return {"<key>": example_for(val, seen, depth + 1)}

    if is_model(tp):
        return example_model(cast("type[BaseModel]", tp), seen, depth)

    if is_typeddict(tp):
        return example_typeddict(tp, seen, depth)

    if isinstance(tp, type) and issubclass(tp, enum.Enum):
        members = list(tp)
        return members[0].value if members else "..."

    if tp is bool:
        return False
    if tp is int:
        return 0
    if tp is float:
        return 0.0
    if tp in (str, bytes):
        return "string"
    if tp in (datetime.datetime,):
        return "2024-01-01T00:00:00Z"
    if tp in (datetime.date,):
        return "2024-01-01"
    if tp is type(None):
        return None
    # object / Any / unmapped -> arbitrary JSON
    return {}


def example_model(tp: "type[BaseModel]", seen: frozenset[str], depth: int) -> Any:
    if tp.__name__ in seen:
        return {"...": f"<recursive {tp.__name__}>"}
    seen = seen | {tp.__name__}
    out: Dict[str, Any] = {}
    for name, field in tp.model_fields.items():
        key = field.alias or name
        out[key] = example_for(field.annotation, seen, depth + 1)
    return out


def example_typeddict(tp: Any, seen: frozenset[str], depth: int) -> Any:
    if getattr(tp, "__name__", "") in seen:
        return {"...": f"<recursive {tp.__name__}>"}
    seen = seen | {getattr(tp, "__name__", "")}
    hints = typing.get_type_hints(tp, include_extras=True)
    out: Dict[str, Any] = {}
    for name, ann in hints.items():
        meta = unwrap_annotated(ann)[1]
        key = alias_from_metadata(meta) or name
        # example_for unwraps Annotated / Required / NotRequired itself.
        out[key] = example_for(ann, seen, depth + 1)
    return out


def render_json(value: Any) -> str:
    return json.dumps(value, indent=2, ensure_ascii=False)


def top_level_examples(name: str) -> List[Tuple[str, Any]]:
    """Return (label, example) pairs for a top-level type name.

    Unions expand to one entry per variant; List[Model] shows one element;
    plain models / aliases yield a single entry."""
    obj = getattr(types_mod, name, None)
    if obj is None:
        return []

    real, _meta = unwrap_annotated(obj)
    origin = tpx.get_origin(real)
    args = tpx.get_args(real)

    if origin in UNION_ORIGINS:
        variants = [a for a in args if a is not type(None)]
        pairs: List[Tuple[str, Any]] = []
        for v in variants:
            v_real, _ = unwrap_annotated(v)
            label = getattr(v_real, "__name__", name)
            pairs.append((label, example_for(v, frozenset(), 0)))
        return pairs

    return [(name, example_for(obj, frozenset(), 0))]


def parse_sections() -> List[Tuple[str, List[str]]]:
    """Parse api.md into ordered (section title, [type names]) pairs."""
    text = API_MD.read_text(encoding="utf-8")
    sections: List[Tuple[str, List[str]]] = []
    current = "Shared Types"
    names: List[str] = []
    for block in re.finditer(r"(?m)^# (.+)$|```python\n(from opencode_ai\.types import[\s\S]*?)\n```", text):
        heading, imports = block.group(1), block.group(2)
        if heading is not None:
            if names:
                sections.append((current, names))
                names = []
            current = heading.strip()
        elif imports is not None:
            import_tree = __import__("ast").parse(imports)
            for node in import_tree.body:
                if isinstance(node, __import__("ast").ImportFrom):
                    names.extend(a.name for a in node.names)
    if names:
        sections.append((current, names))
    return sections


def main() -> int:
    sections = parse_sections()
    lines: List[str] = [
        "# Type Examples",
        "",
        "Auto-generated by `scripts/gen_type_examples.py`. Each block is an example",
        "payload with **every** field populated (required and optional), in wire",
        "shape, so you can see at a glance what a type can contain. Values are",
        "type-indicating placeholders, not real data. Discriminated unions are",
        "expanded to one example per variant.",
        "",
    ]
    flat: Dict[str, Any] = {}
    total = 0
    for title, names in sections:
        lines.append(f"## {title}")
        lines.append("")
        for name in names:
            try:
                pairs = top_level_examples(name)
            except Exception as exc:  # keep going; note the failure
                lines.append(f"<!-- could not render {name}: {exc} -->")
                lines.append("")
                continue
            for label, value in pairs:
                lines.append(f"### {label}")
                lines.append("")
                lines.append("```json")
                lines.append(render_json(value))
                lines.append("```")
                lines.append("")
                flat.setdefault(label, value)
                total += 1
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")
    OUT_JSON.write_text(json.dumps(flat, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {OUT_MD.relative_to(REPO_ROOT).as_posix()} ({total} examples)")
    print(f"wrote {OUT_JSON.relative_to(REPO_ROOT).as_posix()} ({len(flat)} keys)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
