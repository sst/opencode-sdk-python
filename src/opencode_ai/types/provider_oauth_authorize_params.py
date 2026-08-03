# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ProviderOAuthAuthorizeParams"]


class ProviderOAuthAuthorizeParams(TypedDict, total=False):
    method: Required[float]
    """Auth method index"""

    inputs: Dict[str, str]
