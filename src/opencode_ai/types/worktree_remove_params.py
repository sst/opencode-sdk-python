# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WorktreeRemoveParams"]


class WorktreeRemoveParams(TypedDict, total=False):
    directory: Required[str]
    """Directory of the worktree to remove.

    Note: this is a request body field, distinct from the `directory` query
    parameter that may also be present on this same request.
    """
