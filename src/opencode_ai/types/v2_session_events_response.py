# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.


from .._models import BaseModel

__all__ = ["V2SessionEventsResponse"]


class V2SessionEventsResponse(BaseModel):
    id: str

    event: str

    data: str
