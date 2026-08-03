# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Dict, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExperimentalResourceListResponse", "McpResource"]


class McpResource(BaseModel):
    name: str

    uri: str

    client: str

    description: Optional[str] = None

    mime_type: Optional[str] = FieldInfo(alias="mimeType", default=None)


ExperimentalResourceListResponse: TypeAlias = Dict[str, McpResource]
