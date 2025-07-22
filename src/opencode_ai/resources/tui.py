# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import tui_append_prompt_params
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
from ..types.tui_open_help_response import TuiOpenHelpResponse
from ..types.tui_append_prompt_response import TuiAppendPromptResponse

__all__ = ["TuiResource", "AsyncTuiResource"]


class TuiResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TuiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return TuiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TuiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return TuiResourceWithStreamingResponse(self)

    def append_prompt(
        self,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiAppendPromptResponse:
        """
        Append prompt to the TUI

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tui/append-prompt",
            body=maybe_transform({"text": text}, tui_append_prompt_params.TuiAppendPromptParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TuiAppendPromptResponse,
        )

    def open_help(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiOpenHelpResponse:
        """Open the help dialog"""
        return self._post(
            "/tui/open-help",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TuiOpenHelpResponse,
        )


class AsyncTuiResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTuiResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTuiResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTuiResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncTuiResourceWithStreamingResponse(self)

    async def append_prompt(
        self,
        *,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiAppendPromptResponse:
        """
        Append prompt to the TUI

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tui/append-prompt",
            body=await async_maybe_transform({"text": text}, tui_append_prompt_params.TuiAppendPromptParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TuiAppendPromptResponse,
        )

    async def open_help(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiOpenHelpResponse:
        """Open the help dialog"""
        return await self._post(
            "/tui/open-help",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TuiOpenHelpResponse,
        )


class TuiResourceWithRawResponse:
    def __init__(self, tui: TuiResource) -> None:
        self._tui = tui

        self.append_prompt = to_raw_response_wrapper(
            tui.append_prompt,
        )
        self.open_help = to_raw_response_wrapper(
            tui.open_help,
        )


class AsyncTuiResourceWithRawResponse:
    def __init__(self, tui: AsyncTuiResource) -> None:
        self._tui = tui

        self.append_prompt = async_to_raw_response_wrapper(
            tui.append_prompt,
        )
        self.open_help = async_to_raw_response_wrapper(
            tui.open_help,
        )


class TuiResourceWithStreamingResponse:
    def __init__(self, tui: TuiResource) -> None:
        self._tui = tui

        self.append_prompt = to_streamed_response_wrapper(
            tui.append_prompt,
        )
        self.open_help = to_streamed_response_wrapper(
            tui.open_help,
        )


class AsyncTuiResourceWithStreamingResponse:
    def __init__(self, tui: AsyncTuiResource) -> None:
        self._tui = tui

        self.append_prompt = async_to_streamed_response_wrapper(
            tui.append_prompt,
        )
        self.open_help = async_to_streamed_response_wrapper(
            tui.open_help,
        )
