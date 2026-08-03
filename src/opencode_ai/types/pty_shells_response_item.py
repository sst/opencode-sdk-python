# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from .._models import BaseModel

__all__ = ["PtyShellsResponseItem"]


class PtyShellsResponseItem(BaseModel):
    acceptable: bool

    name: str

    path: str
