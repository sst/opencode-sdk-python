# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import TypedDict

from .v2_location_query_params import V2Location

__all__ = ["V2FsListParams"]


class V2FsListParams(TypedDict, total=False):
    location: V2Location

    path: str
