# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing_extensions import Literal

from .._models import BaseModel
from .file_part_source_text import FilePartSourceText

__all__ = ["FileSource"]


class FileSource(BaseModel):
    path: str

    text: FilePartSourceText

    type: Literal["file"]
