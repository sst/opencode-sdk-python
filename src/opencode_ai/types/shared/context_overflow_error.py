# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ContextOverflowError", "Data"]


class Data(BaseModel):
    message: str

    response_body: Optional[str] = FieldInfo(alias="responseBody", default=None)


class ContextOverflowError(BaseModel):
    data: Data

    name: Literal["ContextOverflowError"]
