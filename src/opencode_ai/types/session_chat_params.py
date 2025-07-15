# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .file_part_param import FilePartParam
from .text_part_param import TextPartParam

__all__ = ["SessionChatParams", "Part"]


class SessionChatParams(TypedDict, total=False):
    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    mode: Required[str]

    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]

    parts: Required[Iterable[Part]]

    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]


Part: TypeAlias = Union[FilePartParam, TextPartParam]
