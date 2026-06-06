# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .session_chat_params import ModelParam

__all__ = ["SessionInitParams"]


class SessionInitParams(TypedDict, total=False):
    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    model: Required[ModelParam]
