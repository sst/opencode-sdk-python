# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Command"]


class Command(BaseModel):
    hints: List[str]

    name: str

    template: str

    agent: Optional[str] = None

    description: Optional[str] = None

    model: Optional[str] = None

    source: Optional[Literal["command", "mcp", "skill"]] = None

    subtask: Optional[bool] = None
