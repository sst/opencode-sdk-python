# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Project", "Commands", "Icon", "Time"]


class Commands(BaseModel):
    start: Optional[str] = None
    """Startup script to run when creating a new workspace (worktree)"""


class Icon(BaseModel):
    color: Optional[str] = None

    override: Optional[str] = None

    url: Optional[str] = None


class Time(BaseModel):
    created: float

    updated: float

    initialized: Optional[float] = None


class Project(BaseModel):
    id: str

    sandboxes: List[str]

    time: Time

    worktree: str

    commands: Optional[Commands] = None

    icon: Optional[Icon] = None

    name: Optional[str] = None

    vcs: Optional[Literal["git"]] = None
