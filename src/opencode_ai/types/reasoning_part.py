# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ReasoningPart", "Time"]


class Time(BaseModel):
    start: float

    end: Optional[float] = None


class ReasoningPart(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    session_id: str = FieldInfo(alias="sessionID")

    text: str

    time: Time

    type: Literal["reasoning"]

    metadata: Optional[Dict[str, object]] = None
