# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List
from typing_extensions import TypeAlias

from .vcs_file_status import VcsFileStatus

__all__ = ["VcsStatusResponse"]

VcsStatusResponse: TypeAlias = List[VcsFileStatus]
