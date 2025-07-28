# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["ModeConfig"]


class ModeConfig(BaseModel):
    disable: Optional[bool] = None

    model: Optional[str] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None

    tools: Optional[Dict[str, bool]] = None
