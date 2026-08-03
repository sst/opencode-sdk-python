# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WorktreeResetParams"]


class WorktreeResetParams(TypedDict, total=False):
    directory: Required[str]
    """Directory of the worktree to reset.

    Note: this is a request body field, distinct from the `directory` query
    parameter that may also be present on this same request.
    """
