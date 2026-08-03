# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Optional

from .._models import BaseModel

__all__ = ["VcsInfo"]


class VcsInfo(BaseModel):
    branch: Optional[str] = None

    default_branch: Optional[str] = None
