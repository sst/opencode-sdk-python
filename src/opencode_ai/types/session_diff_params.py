# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionDiffParams"]


class SessionDiffParams(TypedDict, total=False):
    message_id: Annotated[str, PropertyInfo(alias="messageID")]

    directory: str

    workspace: str
