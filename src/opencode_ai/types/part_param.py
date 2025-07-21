# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .file_part_param import FilePartParam
from .text_part_param import TextPartParam
from .tool_part_param import ToolPartParam
from .snapshot_part_param import SnapshotPartParam
from .step_start_part_param import StepStartPartParam
from .step_finish_part_param import StepFinishPartParam

__all__ = ["PartParam"]

PartParam: TypeAlias = Union[
    TextPartParam, FilePartParam, ToolPartParam, StepStartPartParam, StepFinishPartParam, SnapshotPartParam
]
