# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["TextPartInputParam", "Time"]


class Time(TypedDict, total=False):
    start: Required[float]

    end: float


class TextPartInputParam(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]

    id: str

    synthetic: bool

    time: Time
