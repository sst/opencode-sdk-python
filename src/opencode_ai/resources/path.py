# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import path_get_params
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
from ..types.path import Path
from .._base_client import make_request_options

__all__ = ["PathResource", "AsyncPathResource"]


class PathResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PathResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return PathResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PathResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return PathResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Path:
        """
        Get the current path

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/path",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, path_get_params.PathGetParams),
            ),
            cast_to=Path,
        )


class AsyncPathResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPathResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPathResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPathResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncPathResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Path:
        """
        Get the current path

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/path",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, path_get_params.PathGetParams),
            ),
            cast_to=Path,
        )


class PathResourceWithRawResponse:
    def __init__(self, path: PathResource) -> None:
        self._path = path

        self.get = to_raw_response_wrapper(
            path.get,
        )


class AsyncPathResourceWithRawResponse:
    def __init__(self, path: AsyncPathResource) -> None:
        self._path = path

        self.get = async_to_raw_response_wrapper(
            path.get,
        )


class PathResourceWithStreamingResponse:
    def __init__(self, path: PathResource) -> None:
        self._path = path

        self.get = to_streamed_response_wrapper(
            path.get,
        )


class AsyncPathResourceWithStreamingResponse:
    def __init__(self, path: AsyncPathResource) -> None:
        self._path = path

        self.get = async_to_streamed_response_wrapper(
            path.get,
        )
