# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
