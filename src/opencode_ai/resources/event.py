# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from .._base_client import make_request_options
from ..types.event_list_response import EventListResponse

__all__ = ["EventResource", "AsyncEventResource"]


class EventResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return EventResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return EventResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[EventListResponse]:
        """Get events"""
        return self._get(
            "/event",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(Any, EventListResponse),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=Stream[EventListResponse],
        )


class AsyncEventResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEventResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncEventResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[EventListResponse]:
        """Get events"""
        return await self._get(
            "/event",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=cast(Any, EventListResponse),  # Union types cannot be passed in as arguments in the type system
            stream=True,
            stream_cls=AsyncStream[EventListResponse],
        )


class EventResourceWithRawResponse:
    def __init__(self, event: EventResource) -> None:
        self._event = event

        self.list = to_raw_response_wrapper(
            event.list,
        )


class AsyncEventResourceWithRawResponse:
    def __init__(self, event: AsyncEventResource) -> None:
        self._event = event

        self.list = async_to_raw_response_wrapper(
            event.list,
        )


class EventResourceWithStreamingResponse:
    def __init__(self, event: EventResource) -> None:
        self._event = event

        self.list = to_streamed_response_wrapper(
            event.list,
        )


class AsyncEventResourceWithStreamingResponse:
    def __init__(self, event: AsyncEventResource) -> None:
        self._event = event

        self.list = async_to_streamed_response_wrapper(
            event.list,
        )
