# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["V2LocationQueryParams", "V2Location"]


class V2Location(TypedDict, total=False):
    directory: str

    workspace: str


class V2LocationQueryParams(TypedDict, total=False):
    location: V2Location
