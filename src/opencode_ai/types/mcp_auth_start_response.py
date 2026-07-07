# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["McpAuthStartResponse"]


class McpAuthStartResponse(BaseModel):
    authorization_url: str = FieldInfo(alias="authorizationUrl")

    oauth_state: str = FieldInfo(alias="oauthState")
