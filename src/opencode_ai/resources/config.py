# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List
from typing_extensions import Literal

import httpx

from ..types import config_update_params
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
from ..types.config import Config

__all__ = ["ConfigResource", "AsyncConfigResource"]


class ConfigResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return ConfigResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Config:
        """Get config info"""
        return self._get(
            "/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Config,
        )

    def update(
        self,
        *,
        schema_: str | NotGiven = NOT_GIVEN,
        agent: config_update_params.Agent | NotGiven = NOT_GIVEN,
        autoshare: bool | NotGiven = NOT_GIVEN,
        autoupdate: bool | NotGiven = NOT_GIVEN,
        disabled_providers: List[str] | NotGiven = NOT_GIVEN,
        experimental: config_update_params.Experimental | NotGiven = NOT_GIVEN,
        instructions: List[str] | NotGiven = NOT_GIVEN,
        keybinds: config_update_params.Keybinds | NotGiven = NOT_GIVEN,
        layout: Literal["auto", "stretch"] | NotGiven = NOT_GIVEN,
        mcp: Dict[str, config_update_params.Mcp] | NotGiven = NOT_GIVEN,
        mode: config_update_params.Mode | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        provider: config_update_params.Provider | NotGiven = NOT_GIVEN,
        share: Literal["manual", "auto", "disabled"] | NotGiven = NOT_GIVEN,
        small_model: str | NotGiven = NOT_GIVEN,
        theme: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Config:
        """
        Update OpenCode configuration settings and preferences.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/config",
            body=maybe_transform(
                {
                    "schema_": schema_,
                    "agent": agent,
                    "autoshare": autoshare,
                    "autoupdate": autoupdate,
                    "disabled_providers": disabled_providers,
                    "experimental": experimental,
                    "instructions": instructions,
                    "keybinds": keybinds,
                    "layout": layout,
                    "mcp": mcp,
                    "mode": mode,
                    "model": model,
                    "provider": provider,
                    "share": share,
                    "small_model": small_model,
                    "theme": theme,
                    "username": username,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Config,
        )


class AsyncConfigResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncConfigResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Config:
        """Get config info"""
        return await self._get(
            "/config",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Config,
        )

    async def update(
        self,
        *,
        schema_: str | NotGiven = NOT_GIVEN,
        agent: config_update_params.Agent | NotGiven = NOT_GIVEN,
        autoshare: bool | NotGiven = NOT_GIVEN,
        autoupdate: bool | NotGiven = NOT_GIVEN,
        disabled_providers: List[str] | NotGiven = NOT_GIVEN,
        experimental: config_update_params.Experimental | NotGiven = NOT_GIVEN,
        instructions: List[str] | NotGiven = NOT_GIVEN,
        keybinds: config_update_params.Keybinds | NotGiven = NOT_GIVEN,
        layout: Literal["auto", "stretch"] | NotGiven = NOT_GIVEN,
        mcp: Dict[str, config_update_params.Mcp] | NotGiven = NOT_GIVEN,
        mode: config_update_params.Mode | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        provider: config_update_params.Provider | NotGiven = NOT_GIVEN,
        share: Literal["manual", "auto", "disabled"] | NotGiven = NOT_GIVEN,
        small_model: str | NotGiven = NOT_GIVEN,
        theme: str | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Config:
        """
        Update OpenCode configuration settings and preferences.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/config",
            body=await async_maybe_transform(
                {
                    "schema_": schema_,
                    "agent": agent,
                    "autoshare": autoshare,
                    "autoupdate": autoupdate,
                    "disabled_providers": disabled_providers,
                    "experimental": experimental,
                    "instructions": instructions,
                    "keybinds": keybinds,
                    "layout": layout,
                    "mcp": mcp,
                    "mode": mode,
                    "model": model,
                    "provider": provider,
                    "share": share,
                    "small_model": small_model,
                    "theme": theme,
                    "username": username,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Config,
        )


class ConfigResourceWithRawResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.get = to_raw_response_wrapper(
            config.get,
        )
        self.update = to_raw_response_wrapper(
            config.update,
        )


class AsyncConfigResourceWithRawResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.get = async_to_raw_response_wrapper(
            config.get,
        )
        self.update = async_to_raw_response_wrapper(
            config.update,
        )


class ConfigResourceWithStreamingResponse:
    def __init__(self, config: ConfigResource) -> None:
        self._config = config

        self.get = to_streamed_response_wrapper(
            config.get,
        )
        self.update = to_streamed_response_wrapper(
            config.update,
        )


class AsyncConfigResourceWithStreamingResponse:
    def __init__(self, config: AsyncConfigResource) -> None:
        self._config = config

        self.get = async_to_streamed_response_wrapper(
            config.get,
        )
        self.update = async_to_streamed_response_wrapper(
            config.update,
        )
