# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["V2SessionPermissionReplyParams"]


class V2SessionPermissionReplyParams(TypedDict, total=False):
    reply: Required[Literal["once", "always", "reject"]]

    message: str
