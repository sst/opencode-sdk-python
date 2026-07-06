# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
