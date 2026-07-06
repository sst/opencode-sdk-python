# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProjectUpdateParams", "Commands", "Icon"]


class Commands(TypedDict, total=False):
    start: str
    """Startup script to run when creating a new workspace (worktree)"""


class Icon(TypedDict, total=False):
    color: str

    override: str

    url: str


class ProjectUpdateParams(TypedDict, total=False):
    commands: Commands

    icon: Icon

    name: str
