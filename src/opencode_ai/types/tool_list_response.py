# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Dict, List
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["ToolListResponse", "ToolListResponseItem"]


class ToolListResponseItem(BaseModel):
    """A single tool available to the given model, as returned by `GET /experimental/tool`."""

    id: str

    description: str

    parameters: Dict[str, object]
    """The tool's JSON Schema parameter definition."""


ToolListResponse: TypeAlias = List[ToolListResponseItem]
