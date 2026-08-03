# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ProviderAuthAuthorization"]


class ProviderAuthAuthorization(BaseModel):
    instructions: str

    method: Literal["auto", "code"]

    url: str
