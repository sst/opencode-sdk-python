# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AppLogParams"]


class AppLogParams(TypedDict, total=False):
    level: Required[Literal["debug", "info", "error", "warn"]]
    """Log level"""

    message: Required[str]
    """Log message"""

    service: Required[str]
    """Service name for the log entry"""

    extra: Dict[str, object]
    """Additional metadata for the log entry"""
