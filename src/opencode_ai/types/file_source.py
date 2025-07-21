# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel
from .file_part_source_text import FilePartSourceText

__all__ = ["FileSource"]


class FileSource(BaseModel):
    path: str

    text: FilePartSourceText

    type: Literal["file"]
