# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .file_part_input_param import FilePartInputParam
from .text_part_input_param import TextPartInputParam

__all__ = ["SessionPromptParams", "Model", "Part"]


class Model(TypedDict, total=False):
    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]

    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]


class SessionPromptParams(TypedDict, total=False):
    parts: Required[Iterable[Part]]

    model: Model

    agent: str

    message_id: Annotated[str, PropertyInfo(alias="messageID")]

    no_reply: Annotated[bool, PropertyInfo(alias="noReply")]

    tools: Dict[str, bool]

    system: str

    variant: str

    # `format` maps to OutputFormat in the spec. Model it from the spec's
    # OutputFormat schema and add it here as: format: <OutputFormatType>


Part: TypeAlias = Union[TextPartInputParam, FilePartInputParam]
