# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ToolStateCompleted", "Time"]


class Time(BaseModel):
    end: float

    start: float


class ToolStateCompleted(BaseModel):
    metadata: Dict[str, object]

    output: str

    status: Literal["completed"]

    time: Time

    title: str

    input: Optional[object] = None
