# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from .._models import BaseModel

__all__ = ["Path"]


class Path(BaseModel):
    config: str

    directory: str

    home: str

    state: str

    worktree: str
