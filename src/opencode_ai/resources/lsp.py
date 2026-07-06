# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import lsp_status_params
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
from ..types.lsp_status_response import LspStatusResponse

__all__ = ["LspResource", "AsyncLspResource"]


class LspResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LspResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return LspResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LspResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return LspResourceWithStreamingResponse(self)

    def status(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LspStatusResponse:
        """
        Get the status of all language server protocol (LSP) clients.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/lsp",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    lsp_status_params.LspStatusParams,
                ),
            ),
            cast_to=LspStatusResponse,
        )


class AsyncLspResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLspResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLspResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLspResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncLspResourceWithStreamingResponse(self)

    async def status(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LspStatusResponse:
        """
        Get the status of all language server protocol (LSP) clients.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/lsp",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "directory": directory,
                        "workspace": workspace,
                    },
                    lsp_status_params.LspStatusParams,
                ),
            ),
            cast_to=LspStatusResponse,
        )


class LspResourceWithRawResponse:
    def __init__(self, lsp: LspResource) -> None:
        self._lsp = lsp

        self.status = to_raw_response_wrapper(
            lsp.status,
        )


class AsyncLspResourceWithRawResponse:
    def __init__(self, lsp: AsyncLspResource) -> None:
        self._lsp = lsp

        self.status = async_to_raw_response_wrapper(
            lsp.status,
        )


class LspResourceWithStreamingResponse:
    def __init__(self, lsp: LspResource) -> None:
        self._lsp = lsp

        self.status = to_streamed_response_wrapper(
            lsp.status,
        )


class AsyncLspResourceWithStreamingResponse:
    def __init__(self, lsp: AsyncLspResource) -> None:
        self._lsp = lsp

        self.status = async_to_streamed_response_wrapper(
            lsp.status,
        )
