# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ToolStateError", "Time"]


class Time(BaseModel):
    end: float

    start: float


class ToolStateError(BaseModel):
    error: str

    status: Literal["error"]

    time: Time

    input: Optional[object] = None
