# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from .._models import BaseModel

__all__ = ["Symbol", "Location", "LocationRange", "LocationRangeEnd", "LocationRangeStart"]


class LocationRangeEnd(BaseModel):
    character: float

    line: float


class LocationRangeStart(BaseModel):
    character: float

    line: float


class LocationRange(BaseModel):
    end: LocationRangeEnd

    start: LocationRangeStart


class Location(BaseModel):
    range: LocationRange

    uri: str


class Symbol(BaseModel):
    kind: float

    location: Location

    name: str
