# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .file_part_source_text_param import FilePartSourceTextParam

__all__ = ["SymbolSourceParam", "Range", "RangeEnd", "RangeStart"]


class RangeEnd(TypedDict, total=False):
    character: Required[float]

    line: Required[float]


class RangeStart(TypedDict, total=False):
    character: Required[float]

    line: Required[float]


class Range(TypedDict, total=False):
    end: Required[RangeEnd]

    start: Required[RangeStart]


class SymbolSourceParam(TypedDict, total=False):
    kind: Required[int]

    name: Required[str]

    path: Required[str]

    range: Required[Range]

    text: Required[FilePartSourceTextParam]

    type: Required[Literal["symbol"]]
