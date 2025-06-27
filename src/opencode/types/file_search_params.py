# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["FileSearchParams"]


class FileSearchParams(TypedDict, total=False):
    query: Required[str]
