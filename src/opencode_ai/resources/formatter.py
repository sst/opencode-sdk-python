# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from .._base_client import make_request_options
from ..types.formatter_status_response import FormatterStatusResponse

__all__ = ["FormatterResource", "AsyncFormatterResource"]


class FormatterResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FormatterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FormatterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FormatterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return FormatterResourceWithStreamingResponse(self)

    def status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormatterStatusResponse:
        """Get the status of all configured code formatters."""
        return self._get(
            "/formatter",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormatterStatusResponse,
        )


class AsyncFormatterResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFormatterResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFormatterResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFormatterResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncFormatterResourceWithStreamingResponse(self)

    async def status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FormatterStatusResponse:
        """Get the status of all configured code formatters."""
        return await self._get(
            "/formatter",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FormatterStatusResponse,
        )


class FormatterResourceWithRawResponse:
    def __init__(self, formatter: FormatterResource) -> None:
        self._formatter = formatter

        self.status = to_raw_response_wrapper(
            formatter.status,
        )


class AsyncFormatterResourceWithRawResponse:
    def __init__(self, formatter: AsyncFormatterResource) -> None:
        self._formatter = formatter

        self.status = async_to_raw_response_wrapper(
            formatter.status,
        )


class FormatterResourceWithStreamingResponse:
    def __init__(self, formatter: FormatterResource) -> None:
        self._formatter = formatter

        self.status = to_streamed_response_wrapper(
            formatter.status,
        )


class AsyncFormatterResourceWithStreamingResponse:
    def __init__(self, formatter: AsyncFormatterResource) -> None:
        self._formatter = formatter

        self.status = async_to_streamed_response_wrapper(
            formatter.status,
        )
