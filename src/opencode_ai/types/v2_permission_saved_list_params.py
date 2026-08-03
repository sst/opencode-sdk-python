# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["V2PermissionSavedListParams"]


class V2PermissionSavedListParams(TypedDict, total=False):
    project_id: Annotated[str, PropertyInfo(alias="projectID")]
