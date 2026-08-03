# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["PtyConnectParams"]


class PtyConnectParams(TypedDict, total=False):
    cursor: str

    ticket: str

    directory: str

    workspace: str
