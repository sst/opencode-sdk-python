# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

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
