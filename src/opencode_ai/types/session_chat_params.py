# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .message_part_param import MessagePartParam

__all__ = ["SessionChatParams"]


class SessionChatParams(TypedDict, total=False):
    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]

    parts: Required[Iterable[MessagePartParam]]

    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]
    """Session ID"""
