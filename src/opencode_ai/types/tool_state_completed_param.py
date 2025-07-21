# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ToolStateCompletedParam", "Time"]


class Time(TypedDict, total=False):
    end: Required[float]

    start: Required[float]


class ToolStateCompletedParam(TypedDict, total=False):
    input: Required[Dict[str, object]]

    metadata: Required[Dict[str, object]]

    output: Required[str]

    status: Required[Literal["completed"]]

    time: Required[Time]

    title: Required[str]
