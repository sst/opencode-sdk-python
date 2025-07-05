# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .text_part import TextPart
from .tool_part import ToolPart
from .step_start_part import StepStartPart

__all__ = ["AssistantMessagePart"]

AssistantMessagePart: TypeAlias = Annotated[
    Union[TextPart, ToolPart, StepStartPart], PropertyInfo(discriminator="type")
]
