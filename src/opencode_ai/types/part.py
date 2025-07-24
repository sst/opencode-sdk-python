# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .file_part import FilePart
from .text_part import TextPart
from .tool_part import ToolPart
from .snapshot_part import SnapshotPart
from .step_start_part import StepStartPart
from .step_finish_part import StepFinishPart

__all__ = ["Part", "PatchPart"]


class PatchPart(BaseModel):
    id: str

    files: List[str]

    hash: str

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    type: Literal["patch"]


Part: TypeAlias = Annotated[
    Union[TextPart, FilePart, ToolPart, StepStartPart, StepFinishPart, SnapshotPart, PatchPart],
    PropertyInfo(discriminator="type"),
]
