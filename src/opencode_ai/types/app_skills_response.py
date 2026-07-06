# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["AppSkillsResponse", "Skill"]


class Skill(BaseModel):
    content: str

    location: str

    name: str

    description: Optional[str] = None


AppSkillsResponse: TypeAlias = List[Skill]
