# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .file_part_input_param import FilePartInputParam
from .text_part_input_param import TextPartInputParam

__all__ = ["ModelParam", "SessionChatParams", "Part"]


class ModelParam(TypedDict, total=False):
    """Model selection parameters nested under the ``model`` key."""

    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]

    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]


class SessionChatParams(TypedDict, total=False):
    model: Required[ModelParam]

    parts: Required[Iterable[Part]]

    message_id: Annotated[str, PropertyInfo(alias="messageID")]

    mode: str

    system: str

    tools: Dict[str, bool]


Part: TypeAlias = Union[TextPartInputParam, FilePartInputParam]
