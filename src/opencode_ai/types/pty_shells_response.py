# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List
from typing_extensions import TypeAlias

from .pty_shells_response_item import PtyShellsResponseItem

__all__ = ["PtyShellsResponse"]

PtyShellsResponse: TypeAlias = List[PtyShellsResponseItem]
