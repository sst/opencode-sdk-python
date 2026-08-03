# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = ["GlobalUpgradeResponse", "GlobalUpgradeSuccess", "GlobalUpgradeFailure"]


class GlobalUpgradeSuccess(BaseModel):
    success: Literal[True]

    version: str


class GlobalUpgradeFailure(BaseModel):
    success: Literal[False]

    error: str


GlobalUpgradeResponse: TypeAlias = Annotated[
    Union[GlobalUpgradeSuccess, GlobalUpgradeFailure],
    PropertyInfo(discriminator="success"),
]
