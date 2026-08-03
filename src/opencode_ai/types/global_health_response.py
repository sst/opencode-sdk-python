# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GlobalHealthResponse"]


class GlobalHealthResponse(BaseModel):
    healthy: Literal[True]

    version: str
