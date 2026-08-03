# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["V2SessionMessagesParams"]


class V2SessionMessagesParams(TypedDict, total=False):
    limit: float

    order: Literal["asc", "desc"]

    cursor: str
