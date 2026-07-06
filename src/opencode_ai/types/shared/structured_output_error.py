# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["StructuredOutputError", "Data"]


class Data(BaseModel):
    message: str

    retries: int


class StructuredOutputError(BaseModel):
    data: Data

    name: Literal["StructuredOutputError"]
