# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SessionMessagesParams"]


class SessionMessagesParams(TypedDict, total=False):
    before: str

    limit: int

    directory: str

    workspace: str
