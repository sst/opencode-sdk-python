# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FileContentResponse"]


class FileContentResponse(BaseModel):
    content: str

    type: Literal["text", "binary"]

    diff: Optional[str] = None

    encoding: Optional[Literal["base64"]] = None

    mime_type: Optional[str] = FieldInfo(alias="mimeType", default=None)

    patch: Optional[object] = None
