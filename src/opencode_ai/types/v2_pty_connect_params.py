# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["V2PtyConnectParams"]


class V2PtyConnectParams(TypedDict, total=False):
    directory: Annotated[str, PropertyInfo(alias="location[directory]")]

    workspace: Annotated[str, PropertyInfo(alias="location[workspace]")]

    cursor: str

    ticket: str
