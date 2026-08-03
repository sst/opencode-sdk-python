# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProviderAuthError", "Data"]


class Data(BaseModel):
    message: str

    provider_id: str = FieldInfo(alias="providerID")


class ProviderAuthError(BaseModel):
    data: Data

    name: Literal["ProviderAuthError"]
