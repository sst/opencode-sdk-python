# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .snapshot_file_diff import SnapshotFileDiff

__all__ = ["SessionDiffResponse"]

SessionDiffResponse: TypeAlias = List[SnapshotFileDiff]
