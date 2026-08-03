# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExperimentalWorkspaceWarpParams"]


class ExperimentalWorkspaceWarpParams(TypedDict, total=False):
    id: Required[Optional[str]]

    session_id: Required[Annotated[str, PropertyInfo(alias="sessionID")]]

    copy_changes: Annotated[bool, PropertyInfo(alias="copyChanges")]
