# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VcsFileDiff"]


class VcsFileDiff(BaseModel):
    additions: float

    deletions: float

    file: str

    patch: Optional[str] = None

    status: Optional[Literal["added", "deleted", "modified"]] = None
