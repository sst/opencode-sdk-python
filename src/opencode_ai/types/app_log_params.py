# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
