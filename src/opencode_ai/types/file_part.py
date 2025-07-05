# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FilePart"]


class FilePart(BaseModel):
    mime: str

    type: Literal["file"]

    url: str

    filename: Optional[str] = None
