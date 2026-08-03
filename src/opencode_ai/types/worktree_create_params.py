# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorktreeCreateParams"]


class WorktreeCreateParams(TypedDict, total=False):
    name: str
    """Name of the worktree to create."""

    start_command: Annotated[str, PropertyInfo(alias="startCommand")]
    """Command to run inside the worktree when it starts."""
