# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Session", "Time", "Share"]


class Time(BaseModel):
    created: float

    updated: float


class Share(BaseModel):
    url: str


class Session(BaseModel):
    id: str

    time: Time

    title: str

    version: str

    parent_id: Optional[str] = FieldInfo(alias="parentID", default=None)

    share: Optional[Share] = None
