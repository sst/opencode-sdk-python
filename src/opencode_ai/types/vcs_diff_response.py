# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .vcs_file_diff import VcsFileDiff

__all__ = ["VcsDiffResponse"]

VcsDiffResponse: TypeAlias = List[VcsFileDiff]
