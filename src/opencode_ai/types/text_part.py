# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["TextPart", "Time"]


class Time(BaseModel):
    start: float

    end: Optional[float] = None


class TextPart(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    text: str

    type: Literal["text"]

    synthetic: Optional[bool] = None

    time: Optional[Time] = None
