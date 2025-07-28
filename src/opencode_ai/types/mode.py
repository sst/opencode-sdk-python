# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Mode", "Model"]


class Model(BaseModel):
    api_model_id: str = FieldInfo(alias="modelID")

    provider_id: str = FieldInfo(alias="providerID")


class Mode(BaseModel):
    name: str

    tools: Dict[str, bool]

    model: Optional[Model] = None

    prompt: Optional[str] = None

    temperature: Optional[float] = None
