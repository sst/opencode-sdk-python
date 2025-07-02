# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["FileStatusResponse", "FileStatusResponseItem"]


class FileStatusResponseItem(BaseModel):
    added: float

    file: str

    removed: float

    status: Literal["added", "deleted", "modified"]


FileStatusResponse: TypeAlias = List[FileStatusResponseItem]
