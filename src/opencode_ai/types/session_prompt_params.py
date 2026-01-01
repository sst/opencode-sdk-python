# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .file_part_input_param import FilePartInputParam
from .text_part_input_param import TextPartInputParam
from .agent_part_input_param import AgentPartInputParam

__all__ = ["SessionPromptParams", "Part", "Model"]


class SessionPromptParams(TypedDict, total=False):
    parts: Required[Iterable[Part]]

    directory: str

    agent: str

    message_id: Annotated[str, PropertyInfo(alias="messageID")]

    model: Model

    system: str

    tools: Dict[str, bool]


Part: TypeAlias = Union[TextPartInputParam, FilePartInputParam, AgentPartInputParam]


class Model(TypedDict, total=False):
    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]

    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]
