# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["Mode"]


class Mode(BaseModel):
    model: Optional[str] = None

    prompt: Optional[str] = None

    tools: Optional[Dict[str, bool]] = None
