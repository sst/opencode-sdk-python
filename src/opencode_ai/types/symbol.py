# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
