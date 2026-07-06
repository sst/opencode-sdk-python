# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SnapshotFileDiff"]


class SnapshotFileDiff(BaseModel):
    additions: float

    deletions: float

    file: Optional[str] = None

    patch: Optional[str] = None

    status: Optional[Literal["added", "deleted", "modified"]] = None
