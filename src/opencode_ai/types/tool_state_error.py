# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Dict
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ToolStateError", "Time"]


class Time(BaseModel):
    end: float

    start: float


class ToolStateError(BaseModel):
    error: str

    input: Dict[str, object]

    status: Literal["error"]

    time: Time
