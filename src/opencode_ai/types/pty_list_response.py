# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List
from typing_extensions import TypeAlias

from .pty import Pty

__all__ = ["PtyListResponse"]

PtyListResponse: TypeAlias = List[Pty]
