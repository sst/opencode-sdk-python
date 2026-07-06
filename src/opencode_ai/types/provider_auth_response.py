# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import TypeAlias

from .provider_auth_method import ProviderAuthMethod

__all__ = ["ProviderAuthResponse"]

ProviderAuthResponse: TypeAlias = Dict[str, List[ProviderAuthMethod]]
