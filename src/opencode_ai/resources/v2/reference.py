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
from ...types.v2_location_query_params import V2Location
from ...types.v2_reference_list_response import V2ReferenceListResponse

__all__ = ["V2ReferenceResource", "AsyncV2ReferenceResource"]


class V2ReferenceResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2ReferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V2ReferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ReferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return V2ReferenceResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ReferenceListResponse:
        """List references"""
        return self._get(
            "/api/reference",
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
            cast_to=V2ReferenceListResponse,
        )


class AsyncV2ReferenceResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2ReferenceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ReferenceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ReferenceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncV2ReferenceResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2ReferenceListResponse:
        """List references"""
        return await self._get(
            "/api/reference",
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
            cast_to=V2ReferenceListResponse,
        )


class V2ReferenceResourceWithRawResponse:
    def __init__(self, reference: V2ReferenceResource) -> None:
        self._reference = reference

        self.list = to_raw_response_wrapper(
            reference.list,
        )


class AsyncV2ReferenceResourceWithRawResponse:
    def __init__(self, reference: AsyncV2ReferenceResource) -> None:
        self._reference = reference

        self.list = async_to_raw_response_wrapper(
            reference.list,
        )


class V2ReferenceResourceWithStreamingResponse:
    def __init__(self, reference: V2ReferenceResource) -> None:
        self._reference = reference

        self.list = to_streamed_response_wrapper(
            reference.list,
        )


class AsyncV2ReferenceResourceWithStreamingResponse:
    def __init__(self, reference: AsyncV2ReferenceResource) -> None:
        self._reference = reference

        self.list = async_to_streamed_response_wrapper(
            reference.list,
        )
