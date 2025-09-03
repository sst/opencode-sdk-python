# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserMessage", "Time"]


class Time(BaseModel):
    created: float


class UserMessage(BaseModel):
    id: str

    role: Literal["user"]

    session_id: str = FieldInfo(alias="sessionID")

    time: Time
