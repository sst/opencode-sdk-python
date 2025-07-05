# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .user_message_part_param import UserMessagePartParam

__all__ = ["SessionChatParams"]


class SessionChatParams(TypedDict, total=False):
    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]

    parts: Required[Iterable[UserMessagePartParam]]

    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]
