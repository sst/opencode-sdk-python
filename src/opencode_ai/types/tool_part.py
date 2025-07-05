# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .tool_state_error import ToolStateError
from .tool_state_pending import ToolStatePending
from .tool_state_running import ToolStateRunning
from .tool_state_completed import ToolStateCompleted

__all__ = ["ToolPart", "State"]

State: TypeAlias = Annotated[
    Union[ToolStatePending, ToolStateRunning, ToolStateCompleted, ToolStateError], PropertyInfo(discriminator="status")
]


class ToolPart(BaseModel):
    id: str

    state: State

    tool: str

    type: Literal["tool"]
