# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.


from .._models import BaseModel
from .v2_location_info import V2LocationInfo

__all__ = ["V2PtyCreateResponse"]


class V2PtyCreateResponse(BaseModel):
    location: V2LocationInfo

    data: object
