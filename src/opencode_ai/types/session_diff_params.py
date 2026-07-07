# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionDiffParams"]


class SessionDiffParams(TypedDict, total=False):
    message_id: Annotated[str, PropertyInfo(alias="messageID")]

    directory: str

    workspace: str
