# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .message import Message

__all__ = ["SessionMessagesResponse"]

SessionMessagesResponse: TypeAlias = List[Message]
