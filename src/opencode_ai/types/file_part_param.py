# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FilePartParam"]


class FilePartParam(TypedDict, total=False):
    mime: Required[str]

    type: Required[Literal["file"]]

    url: Required[str]

    filename: str
