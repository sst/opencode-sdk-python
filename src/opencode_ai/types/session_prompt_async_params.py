# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .file_part_input_param import FilePartInputParam
from .text_part_input_param import TextPartInputParam
from .agent_part_input_param import AgentPartInputParam
from .subtask_part_input_param import SubtaskPartInputParam

__all__ = ["SessionPromptAsyncParams", "Model", "Format", "OutputFormatText", "OutputFormatJsonSchema", "Part"]


class Model(TypedDict, total=False):
    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]

    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]


class OutputFormatText(TypedDict, total=False):
    type: Required[Literal["text"]]


class OutputFormatJsonSchema(TypedDict, total=False):
    type: Required[Literal["json_schema"]]

    # The spec's `JSONSchema` component is an untyped `{"type": "object"}`.
    schema: Required[object]

    retry_count: Annotated[int, PropertyInfo(alias="retryCount")]


Format: TypeAlias = Union[OutputFormatText, OutputFormatJsonSchema]


class SessionPromptAsyncParams(TypedDict, total=False):
    parts: Required[Iterable[Part]]

    agent: str

    format: Format

    message_id: Annotated[str, PropertyInfo(alias="messageID")]

    model: Model

    no_reply: Annotated[bool, PropertyInfo(alias="noReply")]

    system: str

    tools: Dict[str, bool]

    variant: str


Part: TypeAlias = Union[TextPartInputParam, FilePartInputParam, AgentPartInputParam, SubtaskPartInputParam]
