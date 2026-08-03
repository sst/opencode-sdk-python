# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SessionRespondPermissionParams"]


class SessionRespondPermissionParams(TypedDict, total=False):
    response: Required[Literal["once", "always", "reject"]]
