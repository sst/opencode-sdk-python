# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Session", "Time", "Revert", "Share"]


class Time(BaseModel):
    created: float

    updated: float


class Revert(BaseModel):
    message_id: str = FieldInfo(alias="messageID")

    part: float

    snapshot: Optional[str] = None


class Share(BaseModel):
    url: str


class Session(BaseModel):
    id: str

    time: Time

    title: str

    version: str

    parent_id: Optional[str] = FieldInfo(alias="parentID", default=None)

    revert: Optional[Revert] = None

    share: Optional[Share] = None
