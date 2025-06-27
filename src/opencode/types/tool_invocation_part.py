# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .tool_call import ToolCall
from .tool_result import ToolResult
from .tool_partial_call import ToolPartialCall

__all__ = ["ToolInvocationPart", "ToolInvocation"]

ToolInvocation: TypeAlias = Annotated[Union[ToolCall, ToolPartialCall, ToolResult], PropertyInfo(discriminator="state")]


class ToolInvocationPart(BaseModel):
    tool_invocation: ToolInvocation = FieldInfo(alias="toolInvocation")

    type: Literal["tool-invocation"]
