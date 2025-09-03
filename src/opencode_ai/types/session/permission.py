# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Permission", "Time"]


class Time(BaseModel):
    created: float


class Permission(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    metadata: Dict[str, object]

    session_id: str = FieldInfo(alias="sessionID")

    time: Time

    title: str

    type: str

    call_id: Optional[str] = FieldInfo(alias="callID", default=None)

    pattern: Optional[str] = None
