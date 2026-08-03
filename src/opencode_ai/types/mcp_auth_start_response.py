# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["McpAuthStartResponse"]


class McpAuthStartResponse(BaseModel):
    authorization_url: str = FieldInfo(alias="authorizationUrl")

    oauth_state: str = FieldInfo(alias="oauthState")
