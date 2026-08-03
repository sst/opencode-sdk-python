# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ConsoleState"]


class ConsoleState(BaseModel):
    console_managed_providers: List[str] = FieldInfo(alias="consoleManagedProviders")

    switchable_org_count: int = FieldInfo(alias="switchableOrgCount")

    active_org_name: Optional[str] = FieldInfo(alias="activeOrgName", default=None)
