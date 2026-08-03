# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AddressingParams"]


class AddressingParams(TypedDict, total=False):
    directory: str

    workspace: str

    project: str

    subpath: str

    cursor: str
