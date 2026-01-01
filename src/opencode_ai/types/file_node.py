# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileNode"]


class FileNode(BaseModel):
    ignored: bool

    name: str

    path: str

    type: Literal["file", "directory"]
