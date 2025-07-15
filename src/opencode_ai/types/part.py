# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .file_part import FilePart
from .text_part import TextPart
from .tool_part import ToolPart
from .step_start_part import StepStartPart
from .step_finish_part import StepFinishPart

__all__ = ["Part", "UnionMember5"]


class UnionMember5(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    snapshot: str

    type: Literal["snapshot"]


Part: TypeAlias = Union[TextPart, FilePart, ToolPart, StepStartPart, StepFinishPart, UnionMember5]
