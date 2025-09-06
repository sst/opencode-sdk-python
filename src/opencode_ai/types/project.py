# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Project", "Time"]


class Time(BaseModel):
    created: float

    initialized: Optional[float] = None


class Project(BaseModel):
    id: str

    time: Time

    worktree: str

    vcs: Optional[Literal["git"]] = None
