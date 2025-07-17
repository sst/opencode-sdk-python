# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = ["SessionChatParams", "Part", "PartUnionMember0", "PartUnionMember0Time", "PartUnionMember1"]


class SessionChatParams(TypedDict, total=False):
    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]

    parts: Required[Iterable[Part]]

    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    message_id: Annotated[str, PropertyInfo(alias="messageID")]

    mode: str


class PartUnionMember0Time(TypedDict, total=False):
    start: Required[float]

    end: float


class PartUnionMember0(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["text"]]

    id: str

    synthetic: bool

    time: PartUnionMember0Time


class PartUnionMember1(TypedDict, total=False):
    mime: Required[str]

    type: Required[Literal["file"]]

    url: Required[str]

    id: str

    filename: str


Part: TypeAlias = Union[PartUnionMember0, PartUnionMember1]
