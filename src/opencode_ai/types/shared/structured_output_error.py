# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["StructuredOutputError", "Data"]


class Data(BaseModel):
    message: str

    retries: int


class StructuredOutputError(BaseModel):
    data: Data

    name: Literal["StructuredOutputError"]
