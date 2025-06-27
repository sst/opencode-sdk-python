# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["UnknownError", "Data"]


class Data(BaseModel):
    message: str


class UnknownError(BaseModel):
    data: Data

    name: Literal["UnknownError"]
