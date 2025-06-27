# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["TextPart"]


class TextPart(BaseModel):
    text: str

    type: Literal["text"]
