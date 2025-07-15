# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .file_part import FilePart
from .text_part import TextPart
from .tool_part import ToolPart
from .snapshot_part import SnapshotPart
from .step_start_part import StepStartPart
from .step_finish_part import StepFinishPart

__all__ = ["Part"]

Part: TypeAlias = Annotated[
    Union[TextPart, FilePart, ToolPart, StepStartPart, StepFinishPart, SnapshotPart], PropertyInfo(discriminator="type")
]
