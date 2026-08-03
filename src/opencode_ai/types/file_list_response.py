# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["FileListResponse", "FileNode"]


class FileNode(BaseModel):
    name: str

    path: str

    absolute: str

    type: Literal["file", "directory"]

    ignored: bool


FileListResponse: TypeAlias = List[FileNode]
