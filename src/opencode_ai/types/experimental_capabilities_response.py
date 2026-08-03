# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExperimentalCapabilitiesResponse"]


class ExperimentalCapabilitiesResponse(BaseModel):
    background_subagents: bool = FieldInfo(alias="backgroundSubagents")
