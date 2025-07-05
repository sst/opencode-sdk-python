# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ToolStateRunning", "Time"]


class Time(BaseModel):
    start: float


class ToolStateRunning(BaseModel):
    status: Literal["running"]

    time: Time

    input: Optional[object] = None

    metadata: Optional[Dict[str, object]] = None

    title: Optional[str] = None
