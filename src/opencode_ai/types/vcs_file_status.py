# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["VcsFileStatus"]


class VcsFileStatus(BaseModel):
    additions: float

    deletions: float

    file: str

    status: Literal["added", "deleted", "modified"]
