# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["LSPStatus"]


class LSPStatus(BaseModel):
    id: str

    name: str

    root: str

    status: Literal["connected", "error"]
