# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIError", "Data"]


class Data(BaseModel):
    message: str

    is_retryable: bool = FieldInfo(alias="isRetryable")

    metadata: Optional[object] = None

    response_body: Optional[str] = FieldInfo(alias="responseBody", default=None)

    response_headers: Optional[object] = FieldInfo(alias="responseHeaders", default=None)

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)


class APIError(BaseModel):
    data: Data

    name: Literal["APIError"]
