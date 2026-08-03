# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TuiExecuteCommandParams"]


class TuiExecuteCommandParams(TypedDict, total=False):
    command: Required[str]
