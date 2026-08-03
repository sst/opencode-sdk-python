# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List
from typing_extensions import TypeAlias

from .snapshot_file_diff import SnapshotFileDiff

__all__ = ["SessionDiffResponse"]

SessionDiffResponse: TypeAlias = List[SnapshotFileDiff]
