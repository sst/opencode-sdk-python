# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ExperimentalConsoleSwitchOrgParams"]


class ExperimentalConsoleSwitchOrgParams(TypedDict, total=False):
    account_id: Required[Annotated[str, PropertyInfo(alias="accountID")]]

    org_id: Required[Annotated[str, PropertyInfo(alias="orgID")]]
