# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

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
