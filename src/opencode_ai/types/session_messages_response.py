# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .part import Part
from .message import Message
from .._models import BaseModel

__all__ = ["SessionMessagesResponse", "SessionMessagesResponseItem"]


class SessionMessagesResponseItem(BaseModel):
    info: Message

    parts: List[Part]


SessionMessagesResponse: TypeAlias = List[SessionMessagesResponseItem]
