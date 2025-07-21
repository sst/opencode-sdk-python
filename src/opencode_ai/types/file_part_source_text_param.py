# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FilePartSourceTextParam"]


class FilePartSourceTextParam(TypedDict, total=False):
    end: Required[int]

    start: Required[int]

    value: Required[str]
