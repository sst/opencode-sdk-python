# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["VcsInfo"]


class VcsInfo(BaseModel):
    branch: Optional[str] = None

    default_branch: Optional[str] = None
