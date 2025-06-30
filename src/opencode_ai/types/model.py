# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .._models import BaseModel

__all__ = ["Model", "Cost", "Limit"]


class Cost(BaseModel):
    input: float

    output: float

    cache_read: Optional[float] = None

    cache_write: Optional[float] = None


class Limit(BaseModel):
    context: float

    output: float


class Model(BaseModel):
    id: str

    attachment: bool

    cost: Cost

    limit: Limit

    name: str

    options: Dict[str, object]

    reasoning: bool

    release_date: str

    temperature: bool

    tool_call: bool
