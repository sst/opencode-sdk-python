# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

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
