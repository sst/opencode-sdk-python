# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .vcs_file_status import VcsFileStatus

__all__ = ["VcsStatusResponse"]

VcsStatusResponse: TypeAlias = List[VcsFileStatus]
