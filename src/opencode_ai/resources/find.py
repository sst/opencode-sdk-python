# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import find_text_params, find_files_params, find_symbols_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.find_text_response import FindTextResponse
from ..types.find_files_response import FindFilesResponse
from ..types.find_symbols_response import FindSymbolsResponse

__all__ = ["FindResource", "AsyncFindResource"]


class FindResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FindResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return FindResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FindResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return FindResourceWithStreamingResponse(self)

    def files(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FindFilesResponse:
        """
        Find files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/find/file",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query": query}, find_files_params.FindFilesParams),
            ),
            cast_to=FindFilesResponse,
        )

    def symbols(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FindSymbolsResponse:
        """
        Find workspace symbols

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/find/symbol",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"query": query}, find_symbols_params.FindSymbolsParams),
            ),
            cast_to=FindSymbolsResponse,
        )

    def text(
        self,
        *,
        pattern: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FindTextResponse:
        """
        Find text in files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/find",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"pattern": pattern}, find_text_params.FindTextParams),
            ),
            cast_to=FindTextResponse,
        )


class AsyncFindResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFindResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFindResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFindResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncFindResourceWithStreamingResponse(self)

    async def files(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FindFilesResponse:
        """
        Find files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/find/file",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"query": query}, find_files_params.FindFilesParams),
            ),
            cast_to=FindFilesResponse,
        )

    async def symbols(
        self,
        *,
        query: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FindSymbolsResponse:
        """
        Find workspace symbols

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/find/symbol",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"query": query}, find_symbols_params.FindSymbolsParams),
            ),
            cast_to=FindSymbolsResponse,
        )

    async def text(
        self,
        *,
        pattern: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FindTextResponse:
        """
        Find text in files

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/find",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"pattern": pattern}, find_text_params.FindTextParams),
            ),
            cast_to=FindTextResponse,
        )


class FindResourceWithRawResponse:
    def __init__(self, find: FindResource) -> None:
        self._find = find

        self.files = to_raw_response_wrapper(
            find.files,
        )
        self.symbols = to_raw_response_wrapper(
            find.symbols,
        )
        self.text = to_raw_response_wrapper(
            find.text,
        )


class AsyncFindResourceWithRawResponse:
    def __init__(self, find: AsyncFindResource) -> None:
        self._find = find

        self.files = async_to_raw_response_wrapper(
            find.files,
        )
        self.symbols = async_to_raw_response_wrapper(
            find.symbols,
        )
        self.text = async_to_raw_response_wrapper(
            find.text,
        )


class FindResourceWithStreamingResponse:
    def __init__(self, find: FindResource) -> None:
        self._find = find

        self.files = to_streamed_response_wrapper(
            find.files,
        )
        self.symbols = to_streamed_response_wrapper(
            find.symbols,
        )
        self.text = to_streamed_response_wrapper(
            find.text,
        )


class AsyncFindResourceWithStreamingResponse:
    def __init__(self, find: AsyncFindResource) -> None:
        self._find = find

        self.files = async_to_streamed_response_wrapper(
            find.files,
        )
        self.symbols = async_to_streamed_response_wrapper(
            find.symbols,
        )
        self.text = async_to_streamed_response_wrapper(
            find.text,
        )
