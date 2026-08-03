# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

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
