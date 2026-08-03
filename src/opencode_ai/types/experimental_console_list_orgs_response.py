# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExperimentalConsoleListOrgsResponse", "ConsoleOrg"]


class ConsoleOrg(BaseModel):
    account_id: str = FieldInfo(alias="accountID")

    account_email: str = FieldInfo(alias="accountEmail")

    account_url: str = FieldInfo(alias="accountUrl")

    org_id: str = FieldInfo(alias="orgID")

    org_name: str = FieldInfo(alias="orgName")

    active: bool


class ExperimentalConsoleListOrgsResponse(BaseModel):
    orgs: List[ConsoleOrg]
