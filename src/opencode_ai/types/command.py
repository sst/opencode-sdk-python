# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Command"]


class Command(BaseModel):
    name: str

    template: str

    agent: Optional[str] = None

    description: Optional[str] = None

    model: Optional[str] = None
