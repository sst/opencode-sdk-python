# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .file_part_param import FilePartParam
from .text_part_param import TextPartParam
from .reasoning_part_param import ReasoningPartParam
from .source_url_part_param import SourceURLPartParam
from .step_start_part_param import StepStartPartParam
from .tool_invocation_part_param import ToolInvocationPartParam

__all__ = ["MessagePartParam"]

MessagePartParam: TypeAlias = Union[
    TextPartParam, ReasoningPartParam, ToolInvocationPartParam, SourceURLPartParam, FilePartParam, StepStartPartParam
]
