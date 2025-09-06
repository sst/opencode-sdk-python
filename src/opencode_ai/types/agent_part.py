# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentPart", "Source"]


class Source(BaseModel):
    end: int

    start: int

    value: str


class AgentPart(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    name: str

    session_id: str = FieldInfo(alias="sessionID")

    type: Literal["agent"]

    source: Optional[Source] = None
