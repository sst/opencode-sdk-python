# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["V2ProjectCopyCreateParams"]


class V2ProjectCopyCreateParams(TypedDict, total=False):
    strategy: Required[str]

    directory: Required[str]

    name: str
