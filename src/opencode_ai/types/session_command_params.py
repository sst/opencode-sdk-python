# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionCommandParams"]


class SessionCommandParams(TypedDict, total=False):
    arguments: Required[str]

    command: Required[str]

    directory: str

    agent: str

    message_id: Annotated[str, PropertyInfo(alias="messageID")]

    model: str
