# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["ProviderOAuthAuthorizeParams"]


class ProviderOAuthAuthorizeParams(TypedDict, total=False):
    method: Required[float]
    """Auth method index"""

    inputs: Dict[str, str]
