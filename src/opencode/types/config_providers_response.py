# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel
from .provider import Provider

__all__ = ["ConfigProvidersResponse"]


class ConfigProvidersResponse(BaseModel):
    default: Dict[str, str]

    providers: List[Provider]
