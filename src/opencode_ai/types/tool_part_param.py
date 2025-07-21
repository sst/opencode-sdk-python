# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .tool_state_error_param import ToolStateErrorParam
from .tool_state_pending_param import ToolStatePendingParam
from .tool_state_running_param import ToolStateRunningParam
from .tool_state_completed_param import ToolStateCompletedParam

__all__ = ["ToolPartParam", "State"]

State: TypeAlias = Union[ToolStatePendingParam, ToolStateRunningParam, ToolStateCompletedParam, ToolStateErrorParam]


class ToolPartParam(TypedDict, total=False):
    id: Required[str]

    call_id: Required[Annotated[str, PropertyInfo(alias="callID")]]

    message_id: Required[Annotated[str, PropertyInfo(alias="messageID")]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    state: Required[State]

    tool: Required[str]

    type: Required[Literal["tool"]]
