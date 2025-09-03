# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    tui_open_help_params,
    tui_show_toast_params,
    tui_open_models_params,
    tui_open_themes_params,
    tui_clear_prompt_params,
    tui_append_prompt_params,
    tui_open_sessions_params,
    tui_submit_prompt_params,
    tui_execute_command_params,
)
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
from ..types.tui_show_toast_response import TuiShowToastResponse
from ..types.tui_open_models_response import TuiOpenModelsResponse
from ..types.tui_open_themes_response import TuiOpenThemesResponse
from ..types.tui_clear_prompt_response import TuiClearPromptResponse
from ..types.tui_append_prompt_response import TuiAppendPromptResponse
from ..types.tui_open_sessions_response import TuiOpenSessionsResponse
from ..types.tui_submit_prompt_response import TuiSubmitPromptResponse
from ..types.tui_execute_command_response import TuiExecuteCommandResponse

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
        directory: str | NotGiven = NOT_GIVEN,
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, tui_append_prompt_params.TuiAppendPromptParams),
            ),
            cast_to=TuiAppendPromptResponse,
        )

    def clear_prompt(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiClearPromptResponse:
        """
        Clear the prompt

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tui/clear-prompt",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, tui_clear_prompt_params.TuiClearPromptParams),
            ),
            cast_to=TuiClearPromptResponse,
        )

    def execute_command(
        self,
        *,
        command: str,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiExecuteCommandResponse:
        """Execute a TUI command (e.g.

        agent_cycle)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tui/execute-command",
            body=maybe_transform({"command": command}, tui_execute_command_params.TuiExecuteCommandParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, tui_execute_command_params.TuiExecuteCommandParams),
            ),
            cast_to=TuiExecuteCommandResponse,
        )

    def open_help(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiOpenHelpResponse:
        """
        Open the help dialog

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tui/open-help",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, tui_open_help_params.TuiOpenHelpParams),
            ),
            cast_to=TuiOpenHelpResponse,
        )

    def open_models(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiOpenModelsResponse:
        """
        Open the model dialog

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tui/open-models",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, tui_open_models_params.TuiOpenModelsParams),
            ),
            cast_to=TuiOpenModelsResponse,
        )

    def open_sessions(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiOpenSessionsResponse:
        """
        Open the session dialog

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tui/open-sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, tui_open_sessions_params.TuiOpenSessionsParams),
            ),
            cast_to=TuiOpenSessionsResponse,
        )

    def open_themes(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiOpenThemesResponse:
        """
        Open the theme dialog

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tui/open-themes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, tui_open_themes_params.TuiOpenThemesParams),
            ),
            cast_to=TuiOpenThemesResponse,
        )

    def show_toast(
        self,
        *,
        message: str,
        variant: Literal["info", "success", "warning", "error"],
        directory: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiShowToastResponse:
        """
        Show a toast notification in the TUI

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tui/show-toast",
            body=maybe_transform(
                {
                    "message": message,
                    "variant": variant,
                    "title": title,
                },
                tui_show_toast_params.TuiShowToastParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, tui_show_toast_params.TuiShowToastParams),
            ),
            cast_to=TuiShowToastResponse,
        )

    def submit_prompt(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiSubmitPromptResponse:
        """
        Submit the prompt

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/tui/submit-prompt",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, tui_submit_prompt_params.TuiSubmitPromptParams),
            ),
            cast_to=TuiSubmitPromptResponse,
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
        directory: str | NotGiven = NOT_GIVEN,
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, tui_append_prompt_params.TuiAppendPromptParams
                ),
            ),
            cast_to=TuiAppendPromptResponse,
        )

    async def clear_prompt(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiClearPromptResponse:
        """
        Clear the prompt

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tui/clear-prompt",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, tui_clear_prompt_params.TuiClearPromptParams
                ),
            ),
            cast_to=TuiClearPromptResponse,
        )

    async def execute_command(
        self,
        *,
        command: str,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiExecuteCommandResponse:
        """Execute a TUI command (e.g.

        agent_cycle)

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tui/execute-command",
            body=await async_maybe_transform({"command": command}, tui_execute_command_params.TuiExecuteCommandParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, tui_execute_command_params.TuiExecuteCommandParams
                ),
            ),
            cast_to=TuiExecuteCommandResponse,
        )

    async def open_help(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiOpenHelpResponse:
        """
        Open the help dialog

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tui/open-help",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, tui_open_help_params.TuiOpenHelpParams),
            ),
            cast_to=TuiOpenHelpResponse,
        )

    async def open_models(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiOpenModelsResponse:
        """
        Open the model dialog

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tui/open-models",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, tui_open_models_params.TuiOpenModelsParams),
            ),
            cast_to=TuiOpenModelsResponse,
        )

    async def open_sessions(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiOpenSessionsResponse:
        """
        Open the session dialog

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tui/open-sessions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, tui_open_sessions_params.TuiOpenSessionsParams
                ),
            ),
            cast_to=TuiOpenSessionsResponse,
        )

    async def open_themes(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiOpenThemesResponse:
        """
        Open the theme dialog

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tui/open-themes",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, tui_open_themes_params.TuiOpenThemesParams),
            ),
            cast_to=TuiOpenThemesResponse,
        )

    async def show_toast(
        self,
        *,
        message: str,
        variant: Literal["info", "success", "warning", "error"],
        directory: str | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiShowToastResponse:
        """
        Show a toast notification in the TUI

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tui/show-toast",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "variant": variant,
                    "title": title,
                },
                tui_show_toast_params.TuiShowToastParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, tui_show_toast_params.TuiShowToastParams),
            ),
            cast_to=TuiShowToastResponse,
        )

    async def submit_prompt(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TuiSubmitPromptResponse:
        """
        Submit the prompt

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/tui/submit-prompt",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"directory": directory}, tui_submit_prompt_params.TuiSubmitPromptParams
                ),
            ),
            cast_to=TuiSubmitPromptResponse,
        )


class TuiResourceWithRawResponse:
    def __init__(self, tui: TuiResource) -> None:
        self._tui = tui

        self.append_prompt = to_raw_response_wrapper(
            tui.append_prompt,
        )
        self.clear_prompt = to_raw_response_wrapper(
            tui.clear_prompt,
        )
        self.execute_command = to_raw_response_wrapper(
            tui.execute_command,
        )
        self.open_help = to_raw_response_wrapper(
            tui.open_help,
        )
        self.open_models = to_raw_response_wrapper(
            tui.open_models,
        )
        self.open_sessions = to_raw_response_wrapper(
            tui.open_sessions,
        )
        self.open_themes = to_raw_response_wrapper(
            tui.open_themes,
        )
        self.show_toast = to_raw_response_wrapper(
            tui.show_toast,
        )
        self.submit_prompt = to_raw_response_wrapper(
            tui.submit_prompt,
        )


class AsyncTuiResourceWithRawResponse:
    def __init__(self, tui: AsyncTuiResource) -> None:
        self._tui = tui

        self.append_prompt = async_to_raw_response_wrapper(
            tui.append_prompt,
        )
        self.clear_prompt = async_to_raw_response_wrapper(
            tui.clear_prompt,
        )
        self.execute_command = async_to_raw_response_wrapper(
            tui.execute_command,
        )
        self.open_help = async_to_raw_response_wrapper(
            tui.open_help,
        )
        self.open_models = async_to_raw_response_wrapper(
            tui.open_models,
        )
        self.open_sessions = async_to_raw_response_wrapper(
            tui.open_sessions,
        )
        self.open_themes = async_to_raw_response_wrapper(
            tui.open_themes,
        )
        self.show_toast = async_to_raw_response_wrapper(
            tui.show_toast,
        )
        self.submit_prompt = async_to_raw_response_wrapper(
            tui.submit_prompt,
        )


class TuiResourceWithStreamingResponse:
    def __init__(self, tui: TuiResource) -> None:
        self._tui = tui

        self.append_prompt = to_streamed_response_wrapper(
            tui.append_prompt,
        )
        self.clear_prompt = to_streamed_response_wrapper(
            tui.clear_prompt,
        )
        self.execute_command = to_streamed_response_wrapper(
            tui.execute_command,
        )
        self.open_help = to_streamed_response_wrapper(
            tui.open_help,
        )
        self.open_models = to_streamed_response_wrapper(
            tui.open_models,
        )
        self.open_sessions = to_streamed_response_wrapper(
            tui.open_sessions,
        )
        self.open_themes = to_streamed_response_wrapper(
            tui.open_themes,
        )
        self.show_toast = to_streamed_response_wrapper(
            tui.show_toast,
        )
        self.submit_prompt = to_streamed_response_wrapper(
            tui.submit_prompt,
        )


class AsyncTuiResourceWithStreamingResponse:
    def __init__(self, tui: AsyncTuiResource) -> None:
        self._tui = tui

        self.append_prompt = async_to_streamed_response_wrapper(
            tui.append_prompt,
        )
        self.clear_prompt = async_to_streamed_response_wrapper(
            tui.clear_prompt,
        )
        self.execute_command = async_to_streamed_response_wrapper(
            tui.execute_command,
        )
        self.open_help = async_to_streamed_response_wrapper(
            tui.open_help,
        )
        self.open_models = async_to_streamed_response_wrapper(
            tui.open_models,
        )
        self.open_sessions = async_to_streamed_response_wrapper(
            tui.open_sessions,
        )
        self.open_themes = async_to_streamed_response_wrapper(
            tui.open_themes,
        )
        self.show_toast = async_to_streamed_response_wrapper(
            tui.show_toast,
        )
        self.submit_prompt = async_to_streamed_response_wrapper(
            tui.submit_prompt,
        )
