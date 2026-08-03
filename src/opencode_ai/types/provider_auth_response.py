# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Dict, List
from typing_extensions import TypeAlias

from .provider_auth_method import ProviderAuthMethod

__all__ = ["ProviderAuthResponse"]

ProviderAuthResponse: TypeAlias = Dict[str, List[ProviderAuthMethod]]
