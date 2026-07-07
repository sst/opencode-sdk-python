# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .model import Model
from .._models import BaseModel

__all__ = ["ProviderListResponse", "ProviderListResponseProvider"]


class ProviderListResponseProvider(BaseModel):
    """A single AI provider entry as returned by `GET /provider`.

    NOTE: this is intentionally a distinct type from `opencode_ai.types.Provider`
    (which backs `client.app.providers()` / `AppProvidersResponse`). The two
    schemas are independently defined in the spec and have different shapes
    (this one adds `source`/`key`/`options`; the other adds `api`/`npm`), so
    they cannot share a model without silently corrupting one call site or the
    other.
    """

    id: str

    env: List[str]

    models: Dict[str, Model]

    name: str

    options: Dict[str, object]

    source: Literal["env", "config", "custom", "api"]

    key: Optional[str] = None


class ProviderListResponse(BaseModel):
    all: List[ProviderListResponseProvider]

    connected: List[str]

    default: Dict[str, str]
