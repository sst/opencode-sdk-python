# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["ExperimentalWorkspaceCreateParams"]


class ExperimentalWorkspaceCreateParams(TypedDict, total=False):
    type: Required[str]

    id: str

    branch: Optional[str]

    extra: object
