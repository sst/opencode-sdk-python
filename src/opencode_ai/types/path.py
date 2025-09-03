# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["Path"]


class Path(BaseModel):
    config: str

    directory: str

    state: str

    worktree: str
