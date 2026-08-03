# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from typing_extensions import TypedDict

__all__ = ["ExperimentalSessionListParams"]


class ExperimentalSessionListParams(TypedDict, total=False):
    roots: bool

    start: float

    cursor: float

    search: str

    limit: float

    archived: bool

    directory: str

    workspace: str
