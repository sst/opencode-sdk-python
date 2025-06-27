# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ToolCallParam"]


class ToolCallParam(TypedDict, total=False):
    state: Required[Literal["call"]]

    tool_call_id: Required[Annotated[str, PropertyInfo(alias="toolCallId")]]

    tool_name: Required[Annotated[str, PropertyInfo(alias="toolName")]]

    args: object

    step: float
