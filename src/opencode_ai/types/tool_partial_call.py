# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ToolPartialCall"]


class ToolPartialCall(BaseModel):
    state: Literal["partial-call"]

    tool_call_id: str = FieldInfo(alias="toolCallId")

    tool_name: str = FieldInfo(alias="toolName")

    args: Optional[object] = None

    step: Optional[float] = None
