# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PtyShellsResponseItem"]


class PtyShellsResponseItem(BaseModel):
    acceptable: bool

    name: str

    path: str
