# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TextPartParam", "Time"]


class Time(TypedDict, total=False):
    start: Required[float]

    end: float


class TextPartParam(TypedDict, total=False):
    id: Required[str]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    text: Required[str]

    type: Required[Literal["text"]]

    synthetic: bool

    time: Time
