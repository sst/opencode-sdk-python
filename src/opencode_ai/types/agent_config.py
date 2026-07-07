# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .permission_config import PermissionConfig

__all__ = ["AgentConfig"]


class AgentConfig(BaseModel):
    color: Optional[str] = None
    """Hex color code (e.g., #FF5733) or theme color (e.g., primary)"""

    description: Optional[str] = None

    disable: Optional[bool] = None

    hidden: Optional[bool] = None

    max_steps: Optional[int] = FieldInfo(alias="maxSteps", default=None)

    mode: Optional[Literal["subagent", "primary", "all"]] = None

    model: Optional[str] = None

    options: Optional[object] = None

    permission: Optional[PermissionConfig] = None

    prompt: Optional[str] = None

    steps: Optional[int] = None

    temperature: Optional[float] = None

    tools: Optional[Dict[str, bool]] = None

    top_p: Optional[float] = None

    variant: Optional[str] = None
