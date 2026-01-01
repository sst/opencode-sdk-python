# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .part import Part
from .message import Message
from .._models import BaseModel

__all__ = ["SessionMessageResponse"]


class SessionMessageResponse(BaseModel):
    info: Message

    parts: List[Part]
