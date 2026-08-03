# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserMessage", "Time", "Model"]


class Time(BaseModel):
    created: float


class Model(BaseModel):
    api_model_id: str = FieldInfo(alias="modelID")

    provider_id: str = FieldInfo(alias="providerID")

    variant: Optional[str] = None


class UserMessage(BaseModel):
    id: str

    agent: str

    # Precise Model type for the `model` field, matching the spec's UserMessage.model.
    model: Model

    role: Literal["user"]

    session_id: str = FieldInfo(alias="sessionID")

    time: Time

    # Precise OutputFormat model (OutputFormatText | OutputFormatJsonSchema) is deferred; untyped for now.
    format: Optional[object] = None

    # Precise Summary model (including SnapshotFileDiff) is deferred; untyped for now.
    summary: Optional[object] = None

    system: Optional[str] = None

    tools: Optional[Dict[str, bool]] = None
