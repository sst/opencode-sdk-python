# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ToolStateCompleted", "Time"]


class Time(BaseModel):
    end: float

    start: float


class ToolStateCompleted(BaseModel):
    input: Dict[str, object]

    metadata: Dict[str, object]

    output: str

    status: Literal["completed"]

    time: Time

    title: str
