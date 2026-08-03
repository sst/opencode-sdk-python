# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import httpx

from ...types import v2_location_query_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2_location_get_response import V2LocationGetResponse
from ...types.v2_location_query_params import V2Location

__all__ = ["V2LocationResource", "AsyncV2LocationResource"]


class V2LocationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2LocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V2LocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2LocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return V2LocationResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2LocationGetResponse:
        """Get location"""
        return self._get(
            "/api/location",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"location": location},
                    v2_location_query_params.V2LocationQueryParams,
                ),
            ),
            cast_to=V2LocationGetResponse,
        )


class AsyncV2LocationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2LocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2LocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2LocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncV2LocationResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2LocationGetResponse:
        """Get location"""
        return await self._get(
            "/api/location",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"location": location},
                    v2_location_query_params.V2LocationQueryParams,
                ),
            ),
            cast_to=V2LocationGetResponse,
        )


class V2LocationResourceWithRawResponse:
    def __init__(self, location: V2LocationResource) -> None:
        self._location = location

        self.get = to_raw_response_wrapper(
            location.get,
        )


class AsyncV2LocationResourceWithRawResponse:
    def __init__(self, location: AsyncV2LocationResource) -> None:
        self._location = location

        self.get = async_to_raw_response_wrapper(
            location.get,
        )


class V2LocationResourceWithStreamingResponse:
    def __init__(self, location: V2LocationResource) -> None:
        self._location = location

        self.get = to_streamed_response_wrapper(
            location.get,
        )


class AsyncV2LocationResourceWithStreamingResponse:
    def __init__(self, location: AsyncV2LocationResource) -> None:
        self._location = location

        self.get = async_to_streamed_response_wrapper(
            location.get,
        )
