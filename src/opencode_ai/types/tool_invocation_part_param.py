# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .tool_call_param import ToolCallParam
from .tool_result_param import ToolResultParam
from .tool_partial_call_param import ToolPartialCallParam

__all__ = ["ToolInvocationPartParam", "ToolInvocation"]

ToolInvocation: TypeAlias = Union[ToolCallParam, ToolPartialCallParam, ToolResultParam]


class ToolInvocationPartParam(TypedDict, total=False):
    tool_invocation: Required[Annotated[ToolInvocation, PropertyInfo(alias="toolInvocation")]]

    type: Required[Literal["tool-invocation"]]
