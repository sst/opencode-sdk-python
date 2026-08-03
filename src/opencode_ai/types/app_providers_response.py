# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Dict, List

from .._models import BaseModel
from .provider import Provider

__all__ = ["AppProvidersResponse"]


class AppProvidersResponse(BaseModel):
    default: Dict[str, str]

    providers: List[Provider]
