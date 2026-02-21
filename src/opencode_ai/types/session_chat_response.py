# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .part import Part
from .message import Message
from .._models import BaseModel

__all__ = ["SessionChatResponse"]


class SessionChatResponse(BaseModel):
    """Response from POST /session/{id}/message.

    Contains the assistant message metadata and its parts (text, tool calls, etc.).
    """

    info: Message

    parts: List[Part]
