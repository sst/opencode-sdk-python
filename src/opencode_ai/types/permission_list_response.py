# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List
from typing_extensions import TypeAlias

from .permission_request import PermissionRequest

__all__ = ["PermissionListResponse"]

PermissionListResponse: TypeAlias = List[PermissionRequest]
