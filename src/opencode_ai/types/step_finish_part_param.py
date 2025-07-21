# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StepFinishPartParam", "Tokens", "TokensCache"]


class TokensCache(TypedDict, total=False):
    read: Required[float]

    write: Required[float]


class Tokens(TypedDict, total=False):
    cache: Required[TokensCache]

    input: Required[float]

    output: Required[float]

    reasoning: Required[float]


class StepFinishPartParam(TypedDict, total=False):
    id: Required[str]

    cost: Required[float]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    tokens: Required[Tokens]

    type: Required[Literal["step-finish"]]
