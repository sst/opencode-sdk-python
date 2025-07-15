# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["File"]


class File(BaseModel):
    added: int

    path: str

    removed: int

    status: Literal["added", "deleted", "modified"]
