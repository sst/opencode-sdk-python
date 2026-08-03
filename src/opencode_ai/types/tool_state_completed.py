# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

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
