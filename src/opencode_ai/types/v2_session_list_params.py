# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["V2SessionListParams"]


class V2SessionListParams(TypedDict, total=False):
    workspace: str

    limit: float

    order: Literal["asc", "desc"]

    search: str

    directory: str

    project: str

    subpath: str

    cursor: str
