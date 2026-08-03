# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List
from typing_extensions import TypeAlias

from .session import Session

__all__ = ["SessionListResponse"]

SessionListResponse: TypeAlias = List[Session]
