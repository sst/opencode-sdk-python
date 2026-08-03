# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Any, cast

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
from ..._streaming import Stream, AsyncStream
from ..._base_client import make_request_options
from ...types.v2_event_subscribe_response import V2EventSubscribeResponse

__all__ = ["V2EventResource", "AsyncV2EventResource"]


class V2EventResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2EventResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V2EventResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2EventResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return V2EventResourceWithStreamingResponse(self)

    def subscribe(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[V2EventSubscribeResponse]:
        """Subscribe to events"""
        return self._get(
            "/api/event",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=cast(Any, V2EventSubscribeResponse),
            stream=True,
            stream_cls=Stream[V2EventSubscribeResponse],
        )


class AsyncV2EventResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2EventResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2EventResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2EventResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncV2EventResourceWithStreamingResponse(self)

    async def subscribe(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[V2EventSubscribeResponse]:
        """Subscribe to events"""
        return await self._get(
            "/api/event",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=cast(Any, V2EventSubscribeResponse),
            stream=True,
            stream_cls=AsyncStream[V2EventSubscribeResponse],
        )


class V2EventResourceWithRawResponse:
    def __init__(self, event: V2EventResource) -> None:
        self._event = event

        self.subscribe = to_raw_response_wrapper(
            event.subscribe,
        )


class AsyncV2EventResourceWithRawResponse:
    def __init__(self, event: AsyncV2EventResource) -> None:
        self._event = event

        self.subscribe = async_to_raw_response_wrapper(
            event.subscribe,
        )


class V2EventResourceWithStreamingResponse:
    def __init__(self, event: V2EventResource) -> None:
        self._event = event

        self.subscribe = to_streamed_response_wrapper(
            event.subscribe,
        )


class AsyncV2EventResourceWithStreamingResponse:
    def __init__(self, event: AsyncV2EventResource) -> None:
        self._event = event

        self.subscribe = async_to_streamed_response_wrapper(
            event.subscribe,
        )
