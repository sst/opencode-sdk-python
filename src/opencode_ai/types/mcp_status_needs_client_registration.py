# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MCPStatusNeedsClientRegistration"]


class MCPStatusNeedsClientRegistration(BaseModel):
    error: str

    status: Literal["needs_client_registration"]
