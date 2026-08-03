# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .file_part_input_param import FilePartInputParam

__all__ = ["SessionCommandParams"]


class SessionCommandParams(TypedDict, total=False):
    arguments: Required[str]

    command: Required[str]

    agent: str

    message_id: Annotated[str, PropertyInfo(alias="messageID")]

    # Plain model string (e.g. "claude-opus-4-8"), unlike the `{providerID, modelID}`
    # object used by `prompt`/`shell`/`prompt_async`.
    model: str

    variant: str

    # Structurally identical to `FilePartInputParam` (the spec defines this as a
    # fresh inline schema rather than a `$ref`, but the required/optional field
    # set matches exactly), so it is reused directly here.
    parts: Iterable[FilePartInputParam]
