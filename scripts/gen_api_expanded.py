#!/usr/bin/env python
"""Inject expanded type definitions into api.md.

For every resource section in api.md, this reads the `Types:` import block,
then renders each top-level exported type (a pydantic model class or a
`TypeAlias`) the way it is written in the source, with referenced subtype
names turned into links to their definition (`path#Lline`). Nested subtypes
are not expanded inline -- they are linked, per the doc decision.

The rendered output is wrapped in `<pre><code>` (not a fenced ```python block)
because GitHub does not render links inside fenced code blocks. The injected
region is delimited by `<!-- expanded:start -->` / `<!-- expanded:end -->`
markers so re-running this script replaces the region instead of duplicating.

Regenerate with:
    ./.venv/Scripts/python.exe scripts/gen_api_expanded.py

Requires Python 3.9+ (uses ast.unparse).
"""

from __future__ import annotations

import re
import ast
import html
import argparse
from typing import Dict, List, Tuple, Optional, NamedTuple
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TYPES_DIR = REPO_ROOT / "src" / "opencode_ai" / "types"
API_MD = REPO_ROOT / "api.md"

START_MARKER = "<!-- expanded:start -->"
END_MARKER = "<!-- expanded:end -->"

# Names that appear in annotations but are never SDK types worth linking.
NON_TYPES = {
    # typing / typing_extensions constructs
    "Optional", "List", "Union", "Dict", "Literal", "Annotated", "TypeAlias",
    "Any", "Mapping", "Sequence", "Iterable", "Tuple", "Set", "FrozenSet",
    "Type", "Callable", "Final", "ClassVar", "Required", "NotRequired",
    # builtins
    "str", "int", "float", "bool", "bytes", "object", "None", "True", "False",
    "dict", "list", "set", "tuple", "frozenset",
    # SDK internals
    "BaseModel", "FieldInfo", "PropertyInfo", "TypedDict",
}


class Loc(NamedTuple):
    path: str  # e.g. ./src/opencode_ai/types/part.py
    line: int


Index = Dict[str, List[Loc]]


def rel_path(p: Path) -> str:
    return "./" + p.resolve().relative_to(REPO_ROOT).as_posix()


def build_index() -> Index:
    """Map every module-level class / TypeAlias name to its source location(s)."""
    index: Index = {}
    for path in sorted(TYPES_DIR.rglob("*.py")):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except SyntaxError:
            continue
        rel = rel_path(path)
        for node in tree.body:
            names: List[Tuple[str, int]] = []
            if isinstance(node, ast.ClassDef):
                names.append((node.name, node.lineno))
            elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                names.append((node.target.id, node.lineno))
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        names.append((target.id, node.lineno))
            for name, line in names:
                index.setdefault(name, []).append(Loc(rel, line))
    return index


def resolve(name: str, home: str, index: Index) -> Optional[Loc]:
    """Pick the best definition of `name`: same file first, then a non-params
    file (response/shared types over TypedDict param modules), then the first."""
    entries = index.get(name)
    if not entries:
        return None
    for loc in entries:
        if loc.path == home:
            return loc
    for loc in entries:
        if not loc.path.endswith("_params.py"):
            return loc
    return entries[0]


def linkify(src: str, home: str, index: Index, own: str) -> str:
    """HTML-escape `src` and wrap known type names in links to their source."""
    string_spans = [(m.start(), m.end()) for m in re.finditer(r"\"[^\"]*\"|'[^']*'", src)]

    def in_string(i: int) -> bool:
        return any(a <= i < b for a, b in string_spans)

    out: List[str] = []
    last = 0
    for m in re.finditer(r"[A-Za-z_][A-Za-z0-9_]*", src):
        name = m.group()
        if in_string(m.start()) or name == own or name in NON_TYPES:
            continue
        loc = resolve(name, home, index)
        if loc is None:
            continue
        out.append(html.escape(src[last : m.start()], quote=False))
        out.append(f'<a href="{loc.path}#L{loc.line}">{name}</a>')
        last = m.end()
    out.append(html.escape(src[last:], quote=False))
    return "".join(out)


def extract_alias(value: Optional[ast.expr]) -> Optional[str]:
    if not isinstance(value, ast.Call) or not isinstance(value.func, ast.Name):
        return None
    if value.func.id != "FieldInfo":
        return None
    for kw in value.keywords:
        if kw.arg == "alias" and isinstance(kw.value, ast.Constant) and isinstance(kw.value.value, str):
            return kw.value.value
    return None


def render_class(node: ast.ClassDef, home: str, index: Index) -> str:
    bases = ", ".join(ast.unparse(b) for b in node.bases) or "object"
    lines = [f"class {node.name}({html.escape(bases, quote=False)}):"]

    body = list(node.body)
    if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) and isinstance(body[0].value.value, str):
        doc = body[0].value.value.strip()
        lines.append('    """' + html.escape(doc, quote=False) + '"""')

    fields: List[str] = []
    for item in node.body:
        if not isinstance(item, ast.AnnAssign) or not isinstance(item.target, ast.Name):
            continue
        ann = linkify(ast.unparse(item.annotation), home, index, node.name)
        line = f"    {item.target.id}: {ann}"
        alias = extract_alias(item.value)
        if alias:
            line += f'  # wire name: "{html.escape(alias, quote=False)}"'
        fields.append(line)
    if not fields:
        fields.append("    ...")
    return "\n".join(lines + fields)


def unwrap_annotated(node: ast.expr) -> Tuple[ast.expr, Optional[str]]:
    """`Annotated[T, PropertyInfo(discriminator="x")]` -> (T, 'discriminated by "x"')."""
    if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name) and node.value.id == "Annotated":
        sl = node.slice
        if isinstance(sl, ast.Tuple) and sl.elts:
            inner = sl.elts[0]
            note: Optional[str] = None
            for meta in sl.elts[1:]:
                if isinstance(meta, ast.Call) and isinstance(meta.func, ast.Name) and meta.func.id == "PropertyInfo":
                    for kw in meta.keywords:
                        if kw.arg == "discriminator" and isinstance(kw.value, ast.Constant) and isinstance(kw.value.value, str):
                            note = f'discriminated by "{kw.value.value}"'
            return inner, note
    return node, None


def union_members(node: ast.expr) -> Optional[List[ast.expr]]:
    if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name) and node.value.id == "Union":
        sl = node.slice
        if isinstance(sl, ast.Tuple):
            return list(sl.elts)
        return [sl]
    return None


def render_alias(name: str, value: ast.expr, home: str, index: Index) -> str:
    inner, note = unwrap_annotated(value)
    members = union_members(inner)
    if members is not None and len(members) > 1:
        body = "".join(f"    {linkify(ast.unparse(m), home, index, name)},\n" for m in members)
        rendered = f"{name}: TypeAlias = Union[\n{body}]"
    else:
        rendered = f"{name}: TypeAlias = {linkify(ast.unparse(inner), home, index, name)}"
    if note:
        rendered += f"  # {note}"
    return rendered


def find_node(name: str, loc: Loc) -> Optional[ast.stmt]:
    path = REPO_ROOT / loc.path[2:]
    tree = ast.parse(path.read_text(encoding="utf-8"))
    for node in tree.body:
        if node.lineno != loc.line:
            continue
        if isinstance(node, ast.ClassDef) and node.name == name:
            return node
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name) and node.target.id == name:
            return node
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    return node
    return None


def render_top(name: str, index: Index) -> Optional[str]:
    loc = resolve(name, home="", index=index)
    if loc is None:
        return None
    node = find_node(name, loc)
    home = loc.path
    if isinstance(node, ast.ClassDef):
        return render_class(node, home, index)
    if isinstance(node, ast.AnnAssign) and node.value is not None:
        return render_alias(name, node.value, home, index)
    if isinstance(node, ast.Assign):
        return render_alias(name, node.value, home, index)
    return None


def import_names(block_src: str) -> List[str]:
    tree = ast.parse(block_src)
    names: List[str] = []
    for node in tree.body:
        if isinstance(node, ast.ImportFrom):
            names.extend(alias.name for alias in node.names)
    return names


def build_expanded(names: List[str], index: Index) -> str:
    parts: List[str] = [
        START_MARKER,
        "",
        "<details>",
        "<summary>Expanded definitions (top-level types; referenced subtypes link to source)</summary>",
        "",
    ]
    for name in names:
        rendered = render_top(name, index)
        if rendered is None:
            print(f"  warn: could not render {name}")
            continue
        parts.append("<pre><code>" + rendered + "</code></pre>")
        parts.append("")
    parts.append("</details>")
    parts.append("")
    parts.append(END_MARKER)
    return "\n".join(parts)


def strip_existing(text: str) -> str:
    pattern = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL)
    return pattern.sub("", text)


def inject(text: str, index: Index) -> str:
    text = strip_existing(text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    block_re = re.compile(r"```python\n(from opencode_ai\.types import.*?)\n```\n", re.DOTALL)

    def repl(match: "re.Match[str]") -> str:
        names = import_names(match.group(1))
        expanded = build_expanded(names, index)
        return match.group(0) + "\n" + expanded + "\n"

    text = block_re.sub(repl, text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    if not text.endswith("\n"):
        text += "\n"
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if api.md would change")
    args = parser.parse_args()

    index = build_index()
    original = API_MD.read_text(encoding="utf-8")
    updated = inject(original, index)

    if args.check:
        if original != updated:
            print("api.md is out of date; run scripts/gen_api_expanded.py")
            return 1
        print("api.md is up to date")
        return 0

    API_MD.write_text(updated, encoding="utf-8")
    print(f"wrote {rel_path(API_MD)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
