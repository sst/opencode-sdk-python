# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import app_log_params
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
from ..types.app import App
from .._base_client import make_request_options
from ..types.app_log_response import AppLogResponse
from ..types.app_init_response import AppInitResponse
from ..types.app_modes_response import AppModesResponse
from ..types.app_providers_response import AppProvidersResponse

__all__ = ["AppResource", "AsyncAppResource"]


class AppResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AppResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AppResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> App:
        """Get app info"""
        return self._get(
            "/app",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=App,
        )

    def init(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppInitResponse:
        """Initialize the app"""
        return self._post(
            "/app/init",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppInitResponse,
        )

    def log(
        self,
        *,
        level: Literal["debug", "info", "error", "warn"],
        message: str,
        service: str,
        extra: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppLogResponse:
        """
        Write a log entry to the server logs

        Args:
          level: Log level

          message: Log message

          service: Service name for the log entry

          extra: Additional metadata for the log entry

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/log",
            body=maybe_transform(
                {
                    "level": level,
                    "message": message,
                    "service": service,
                    "extra": extra,
                },
                app_log_params.AppLogParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppLogResponse,
        )

    def modes(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppModesResponse:
        """List all modes"""
        return self._get(
            "/mode",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppModesResponse,
        )

    def providers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppProvidersResponse:
        """List all providers"""
        return self._get(
            "/config/providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppProvidersResponse,
        )


class AsyncAppResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncAppResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> App:
        """Get app info"""
        return await self._get(
            "/app",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=App,
        )

    async def init(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppInitResponse:
        """Initialize the app"""
        return await self._post(
            "/app/init",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppInitResponse,
        )

    async def log(
        self,
        *,
        level: Literal["debug", "info", "error", "warn"],
        message: str,
        service: str,
        extra: Dict[str, object] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppLogResponse:
        """
        Write a log entry to the server logs

        Args:
          level: Log level

          message: Log message

          service: Service name for the log entry

          extra: Additional metadata for the log entry

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/log",
            body=await async_maybe_transform(
                {
                    "level": level,
                    "message": message,
                    "service": service,
                    "extra": extra,
                },
                app_log_params.AppLogParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppLogResponse,
        )

    async def modes(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppModesResponse:
        """List all modes"""
        return await self._get(
            "/mode",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppModesResponse,
        )

    async def providers(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppProvidersResponse:
        """List all providers"""
        return await self._get(
            "/config/providers",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AppProvidersResponse,
        )


class AppResourceWithRawResponse:
    def __init__(self, app: AppResource) -> None:
        self._app = app

        self.get = to_raw_response_wrapper(
            app.get,
        )
        self.init = to_raw_response_wrapper(
            app.init,
        )
        self.log = to_raw_response_wrapper(
            app.log,
        )
        self.modes = to_raw_response_wrapper(
            app.modes,
        )
        self.providers = to_raw_response_wrapper(
            app.providers,
        )


class AsyncAppResourceWithRawResponse:
    def __init__(self, app: AsyncAppResource) -> None:
        self._app = app

        self.get = async_to_raw_response_wrapper(
            app.get,
        )
        self.init = async_to_raw_response_wrapper(
            app.init,
        )
        self.log = async_to_raw_response_wrapper(
            app.log,
        )
        self.modes = async_to_raw_response_wrapper(
            app.modes,
        )
        self.providers = async_to_raw_response_wrapper(
            app.providers,
        )


class AppResourceWithStreamingResponse:
    def __init__(self, app: AppResource) -> None:
        self._app = app

        self.get = to_streamed_response_wrapper(
            app.get,
        )
        self.init = to_streamed_response_wrapper(
            app.init,
        )
        self.log = to_streamed_response_wrapper(
            app.log,
        )
        self.modes = to_streamed_response_wrapper(
            app.modes,
        )
        self.providers = to_streamed_response_wrapper(
            app.providers,
        )


class AsyncAppResourceWithStreamingResponse:
    def __init__(self, app: AsyncAppResource) -> None:
        self._app = app

        self.get = async_to_streamed_response_wrapper(
            app.get,
        )
        self.init = async_to_streamed_response_wrapper(
            app.init,
        )
        self.log = async_to_streamed_response_wrapper(
            app.log,
        )
        self.modes = async_to_streamed_response_wrapper(
            app.modes,
        )
        self.providers = async_to_streamed_response_wrapper(
            app.providers,
        )
