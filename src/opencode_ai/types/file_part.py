# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .file_part_source import FilePartSource

__all__ = ["FilePart"]


class FilePart(BaseModel):
    id: str

    message_id: str = FieldInfo(alias="messageID")

    mime: str

    session_id: str = FieldInfo(alias="sessionID")

    type: Literal["file"]

    url: str

    filename: Optional[str] = None

    source: Optional[FilePartSource] = None
