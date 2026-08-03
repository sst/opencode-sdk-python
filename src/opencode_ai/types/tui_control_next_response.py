# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from .._models import BaseModel

__all__ = ["TuiControlNextResponse"]


class TuiControlNextResponse(BaseModel):
    path: str

    body: object
