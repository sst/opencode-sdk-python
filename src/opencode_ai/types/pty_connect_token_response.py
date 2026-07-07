# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["PtyConnectTokenResponse"]


class PtyConnectTokenResponse(BaseModel):
    expires_in: int

    ticket: str
