# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolStateErrorParam", "Time"]


class Time(TypedDict, total=False):
    end: Required[float]

    start: Required[float]


class ToolStateErrorParam(TypedDict, total=False):
    error: Required[str]

    input: Required[Dict[str, object]]

    status: Required[Literal["error"]]

    time: Required[Time]
