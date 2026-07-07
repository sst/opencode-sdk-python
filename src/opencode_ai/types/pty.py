# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Pty"]


class Pty(BaseModel):
    id: str

    args: List[str]

    command: str

    cwd: str

    pid: int

    status: Literal["running", "exited"]

    title: str
