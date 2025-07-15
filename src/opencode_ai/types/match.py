# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["Match", "Lines", "Path", "Submatch", "SubmatchMatch"]


class Lines(BaseModel):
    text: str


class Path(BaseModel):
    text: str


class SubmatchMatch(BaseModel):
    text: str


class Submatch(BaseModel):
    end: float

    match: SubmatchMatch

    start: float


class Match(BaseModel):
    absolute_offset: float

    line_number: float

    lines: Lines

    path: Path

    submatches: List[Submatch]
