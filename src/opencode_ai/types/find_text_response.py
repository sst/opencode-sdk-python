# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = [
    "FindTextResponse",
    "FindTextResponseItem",
    "FindTextResponseItemLines",
    "FindTextResponseItemPath",
    "FindTextResponseItemSubmatch",
    "FindTextResponseItemSubmatchMatch",
]


class FindTextResponseItemLines(BaseModel):
    text: str


class FindTextResponseItemPath(BaseModel):
    text: str


class FindTextResponseItemSubmatchMatch(BaseModel):
    text: str


class FindTextResponseItemSubmatch(BaseModel):
    end: float

    match: FindTextResponseItemSubmatchMatch

    start: float


class FindTextResponseItem(BaseModel):
    absolute_offset: float

    line_number: float

    lines: FindTextResponseItemLines

    path: FindTextResponseItemPath

    submatches: List[FindTextResponseItemSubmatch]


FindTextResponse: TypeAlias = List[FindTextResponseItem]
