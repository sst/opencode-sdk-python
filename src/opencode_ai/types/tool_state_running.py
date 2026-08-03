# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

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
