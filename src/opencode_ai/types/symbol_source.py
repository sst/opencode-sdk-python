# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .file_part_source_text import FilePartSourceText

__all__ = ["SymbolSource", "Range", "RangeEnd", "RangeStart"]


class RangeEnd(BaseModel):
    character: float

    line: float


class RangeStart(BaseModel):
    character: float

    line: float


class Range(BaseModel):
    end: RangeEnd

    start: RangeStart


class SymbolSource(BaseModel):
    kind: int

    name: str

    path: str

    range: Range

    text: FilePartSourceText

    type: Literal["symbol"]
