# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SubtaskPartInputParam", "Model"]


class Model(TypedDict, total=False):
    provider_id: Required[Annotated[str, PropertyInfo(alias="providerID")]]

    model_id: Required[Annotated[str, PropertyInfo(alias="modelID")]]


class SubtaskPartInputParam(TypedDict, total=False):
    agent: Required[str]

    # Not listed under `properties` in the spec (a spec inconsistency -- it is
    # listed in `required` but has no schema of its own) but present on the
    # response-side `SubtaskPart.description` field, so modeled here as a
    # required string to match the required list and the response shape.
    description: Required[str]

    prompt: Required[str]

    type: Required[Literal["subtask"]]

    id: str

    command: str

    model: Model
