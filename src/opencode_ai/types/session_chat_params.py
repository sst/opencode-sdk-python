# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .file_part_input_param import FilePartInputParam
from .text_part_input_param import TextPartInputParam

__all__ = ["SessionChatParams", "Part"]


class SessionChatParams(TypedDict, total=False):
    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]

    parts: Required[Iterable[Part]]

    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    message_id: Annotated[str, PropertyInfo(alias="messageID")]

    mode: str


Part: TypeAlias = Union[TextPartInputParam, FilePartInputParam]
