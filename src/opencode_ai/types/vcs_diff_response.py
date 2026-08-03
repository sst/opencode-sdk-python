# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List
from typing_extensions import TypeAlias

from .vcs_file_diff import VcsFileDiff

__all__ = ["VcsDiffResponse"]

VcsDiffResponse: TypeAlias = List[VcsFileDiff]
