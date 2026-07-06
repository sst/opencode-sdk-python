# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SessionRespondPermissionParams"]


class SessionRespondPermissionParams(TypedDict, total=False):
    response: Required[Literal["once", "always", "reject"]]
