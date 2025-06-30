# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["App", "Path", "Time"]


class Path(BaseModel):
    config: str

    cwd: str

    data: str

    root: str

    state: str


class Time(BaseModel):
    initialized: Optional[float] = None


class App(BaseModel):
    git: bool

    hostname: str

    path: Path

    time: Time

    user: str
