# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .file_part import FilePart
from .text_part import TextPart
from .reasoning_part import ReasoningPart
from .source_url_part import SourceURLPart
from .step_start_part import StepStartPart
from .tool_invocation_part import ToolInvocationPart

__all__ = ["MessagePart"]

MessagePart: TypeAlias = Annotated[
    Union[TextPart, ReasoningPart, ToolInvocationPart, SourceURLPart, FilePart, StepStartPart],
    PropertyInfo(discriminator="type"),
]
