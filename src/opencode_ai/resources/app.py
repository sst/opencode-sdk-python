# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal

import httpx

from ..types import app_log_params, app_providers_params
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
from ..types.app_log_response import AppLogResponse
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

    def log(
        self,
        *,
        level: Literal["debug", "info", "error", "warn"],
        message: str,
        service: str,
        directory: str | NotGiven = NOT_GIVEN,
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, app_log_params.AppLogParams),
            ),
            cast_to=AppLogResponse,
        )

    def providers(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppProvidersResponse:
        """
        List all providers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/config/providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"directory": directory}, app_providers_params.AppProvidersParams),
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

    async def log(
        self,
        *,
        level: Literal["debug", "info", "error", "warn"],
        message: str,
        service: str,
        directory: str | NotGiven = NOT_GIVEN,
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
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, app_log_params.AppLogParams),
            ),
            cast_to=AppLogResponse,
        )

    async def providers(
        self,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppProvidersResponse:
        """
        List all providers

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/config/providers",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"directory": directory}, app_providers_params.AppProvidersParams),
            ),
            cast_to=AppProvidersResponse,
        )


class AppResourceWithRawResponse:
    def __init__(self, app: AppResource) -> None:
        self._app = app

        self.log = to_raw_response_wrapper(
            app.log,
        )
        self.providers = to_raw_response_wrapper(
            app.providers,
        )


class AsyncAppResourceWithRawResponse:
    def __init__(self, app: AsyncAppResource) -> None:
        self._app = app

        self.log = async_to_raw_response_wrapper(
            app.log,
        )
        self.providers = async_to_raw_response_wrapper(
            app.providers,
        )


class AppResourceWithStreamingResponse:
    def __init__(self, app: AppResource) -> None:
        self._app = app

        self.log = to_streamed_response_wrapper(
            app.log,
        )
        self.providers = to_streamed_response_wrapper(
            app.providers,
        )


class AsyncAppResourceWithStreamingResponse:
    def __init__(self, app: AsyncAppResource) -> None:
        self._app = app

        self.log = async_to_streamed_response_wrapper(
            app.log,
        )
        self.providers = async_to_streamed_response_wrapper(
            app.providers,
        )
