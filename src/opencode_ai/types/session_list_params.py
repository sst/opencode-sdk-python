# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["SessionListParams"]


class SessionListParams(TypedDict, total=False):
    limit: float

    path: str

    roots: bool

    scope: Literal["project"]

    search: str

    start: float

    directory: str

    workspace: str
