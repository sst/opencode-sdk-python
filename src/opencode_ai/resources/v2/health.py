# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2_health_get_response import V2HealthGetResponse

__all__ = ["V2HealthResource", "AsyncV2HealthResource"]


class V2HealthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2HealthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V2HealthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2HealthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return V2HealthResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2HealthGetResponse:
        """Check server health"""
        return self._get(
            "/api/health",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2HealthGetResponse,
        )


class AsyncV2HealthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2HealthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2HealthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2HealthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncV2HealthResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2HealthGetResponse:
        """Check server health"""
        return await self._get(
            "/api/health",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=V2HealthGetResponse,
        )


class V2HealthResourceWithRawResponse:
    def __init__(self, health: V2HealthResource) -> None:
        self._health = health

        self.get = to_raw_response_wrapper(
            health.get,
        )


class AsyncV2HealthResourceWithRawResponse:
    def __init__(self, health: AsyncV2HealthResource) -> None:
        self._health = health

        self.get = async_to_raw_response_wrapper(
            health.get,
        )


class V2HealthResourceWithStreamingResponse:
    def __init__(self, health: V2HealthResource) -> None:
        self._health = health

        self.get = to_streamed_response_wrapper(
            health.get,
        )


class AsyncV2HealthResourceWithStreamingResponse:
    def __init__(self, health: AsyncV2HealthResource) -> None:
        self._health = health

        self.get = async_to_streamed_response_wrapper(
            health.get,
        )
