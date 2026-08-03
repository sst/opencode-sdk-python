# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["PtyUpdateParams", "Size"]


class Size(TypedDict, total=False):
    cols: Required[int]

    rows: Required[int]


class PtyUpdateParams(TypedDict, total=False):
    size: Size

    title: str
