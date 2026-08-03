# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GlobalUpgradeParams"]


class GlobalUpgradeParams(TypedDict, total=False):
    """Request body for `POST /global/upgrade`.

    An empty body upgrades to the latest available version.
    """

    target: str
    """Version to upgrade to, e.g. `1.18.12`."""
