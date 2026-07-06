# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .assistant_message import AssistantMessage
from .part import Part

__all__ = ["SessionPromptResponse"]


class SessionPromptResponse(BaseModel):
    info: AssistantMessage

    parts: List[Part]
