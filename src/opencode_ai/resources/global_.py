# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

"""Global server operations (`/global/*`).

`global` is a Python keyword, so the module is named `global_` and the
resource is exposed on the client as `client.global_`.
"""

from __future__ import annotations

from typing import Any, Dict, List, Tuple, Union, cast
from typing_extensions import Literal

import httpx

from ..types import config_update_params, global_upgrade_params
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
from .._streaming import Stream, AsyncStream
from .._base_client import make_request_options
from ..types.config import Config
from ..types.global_event_response import GlobalEventResponse
from ..types.global_health_response import GlobalHealthResponse
from ..types.global_dispose_response import GlobalDisposeResponse
from ..types.global_upgrade_response import GlobalUpgradeResponse
from ..types.global_config_get_response import GlobalConfigGetResponse

__all__ = ["GlobalResource", "AsyncGlobalResource"]


class GlobalConfigResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GlobalConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return GlobalConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return GlobalConfigResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalConfigGetResponse:
        """Get global config info"""
        return self._get(
            "/global/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=GlobalConfigGetResponse,
        )

    def update(
        self,
        *,
        schema_: str | NotGiven = NOT_GIVEN,
        agent: config_update_params.Agent | NotGiven = NOT_GIVEN,
        attachment: config_update_params.Attachment | NotGiven = NOT_GIVEN,
        autoshare: bool | NotGiven = NOT_GIVEN,
        autoupdate: bool | Literal["notify"] | NotGiven = NOT_GIVEN,
        command: Dict[str, config_update_params.CommandConfig] | NotGiven = NOT_GIVEN,
        compaction: config_update_params.Compaction | NotGiven = NOT_GIVEN,
        default_agent: str | NotGiven = NOT_GIVEN,
        disabled_providers: List[str] | NotGiven = NOT_GIVEN,
        enabled_providers: List[str] | NotGiven = NOT_GIVEN,
        enterprise: config_update_params.Enterprise | NotGiven = NOT_GIVEN,
        experimental: config_update_params.Experimental | NotGiven = NOT_GIVEN,
        formatter: bool | Dict[str, config_update_params.FormatterConfig] | NotGiven = NOT_GIVEN,
        instructions: List[str] | NotGiven = NOT_GIVEN,
        layout: Literal["auto", "stretch"] | NotGiven = NOT_GIVEN,
        log_level: Literal["DEBUG", "INFO", "WARN", "ERROR"] | NotGiven = NOT_GIVEN,
        lsp: bool | Dict[str, config_update_params.LspConfig] | NotGiven = NOT_GIVEN,
        mcp: Dict[str, config_update_params.Mcp] | NotGiven = NOT_GIVEN,
        mode: config_update_params.Mode | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        permission: config_update_params.PermissionConfig | NotGiven = NOT_GIVEN,
        plugin: List[Union[str, Tuple[str, object]]] | NotGiven = NOT_GIVEN,
        provider: config_update_params.Provider | NotGiven = NOT_GIVEN,
        reference: Dict[str, config_update_params.ReferenceConfigEntry] | NotGiven = NOT_GIVEN,
        server: config_update_params.Server | NotGiven = NOT_GIVEN,
        share: Literal["manual", "auto", "disabled"] | NotGiven = NOT_GIVEN,
        shell: str | NotGiven = NOT_GIVEN,
        skills: config_update_params.Skills | NotGiven = NOT_GIVEN,
        small_model: str | NotGiven = NOT_GIVEN,
        snapshot: bool | NotGiven = NOT_GIVEN,
        subagent_depth: int | NotGiven = NOT_GIVEN,
        tool_output: config_update_params.ToolOutput | NotGiven = NOT_GIVEN,
        tools: Dict[str, bool] | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        watcher: config_update_params.Watcher | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Config:
        """
        Update global OpenCode configuration settings and preferences.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._patch(
            "/global/config",
            body=maybe_transform(
                {
                    "schema_": schema_,
                    "agent": agent,
                    "attachment": attachment,
                    "autoshare": autoshare,
                    "autoupdate": autoupdate,
                    "command": command,
                    "compaction": compaction,
                    "default_agent": default_agent,
                    "disabled_providers": disabled_providers,
                    "enabled_providers": enabled_providers,
                    "enterprise": enterprise,
                    "experimental": experimental,
                    "formatter": formatter,
                    "instructions": instructions,
                    "layout": layout,
                    "log_level": log_level,
                    "lsp": lsp,
                    "mcp": mcp,
                    "mode": mode,
                    "model": model,
                    "permission": permission,
                    "plugin": plugin,
                    "provider": provider,
                    "reference": reference,
                    "server": server,
                    "share": share,
                    "shell": shell,
                    "skills": skills,
                    "small_model": small_model,
                    "snapshot": snapshot,
                    "subagent_depth": subagent_depth,
                    "tool_output": tool_output,
                    "tools": tools,
                    "username": username,
                    "watcher": watcher,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=Config,
        )


class GlobalResource(SyncAPIResource):
    @cached_property
    def config(self) -> GlobalConfigResource:
        return GlobalConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> GlobalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return GlobalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GlobalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return GlobalResourceWithStreamingResponse(self)

    def health(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalHealthResponse:
        """Get health"""
        return self._get(
            "/global/health",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=GlobalHealthResponse,
        )

    def event(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Stream[GlobalEventResponse]:
        """Get global events"""
        return self._get(
            "/global/event",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=GlobalEventResponse,
            stream=True,
            stream_cls=Stream[GlobalEventResponse],
        )

    def dispose(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalDisposeResponse:
        """Dispose of the global server instance and free its resources."""
        return self._post(
            "/global/dispose",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=GlobalDisposeResponse,
        )

    def upgrade(
        self,
        *,
        target: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalUpgradeResponse:
        """
        Upgrade the OpenCode server.

        Args:
          target: Version to upgrade to; when omitted, upgrades to the latest
              available version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            GlobalUpgradeResponse,
            self._post(
                "/global/upgrade",
                body=maybe_transform(
                    {
                        "target": target,
                    },
                    global_upgrade_params.GlobalUpgradeParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                ),
                cast_to=cast(Any, GlobalUpgradeResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncGlobalConfigResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGlobalConfigResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGlobalConfigResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalConfigResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncGlobalConfigResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalConfigGetResponse:
        """Get global config info"""
        return await self._get(
            "/global/config",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=GlobalConfigGetResponse,
        )

    async def update(
        self,
        *,
        schema_: str | NotGiven = NOT_GIVEN,
        agent: config_update_params.Agent | NotGiven = NOT_GIVEN,
        attachment: config_update_params.Attachment | NotGiven = NOT_GIVEN,
        autoshare: bool | NotGiven = NOT_GIVEN,
        autoupdate: bool | Literal["notify"] | NotGiven = NOT_GIVEN,
        command: Dict[str, config_update_params.CommandConfig] | NotGiven = NOT_GIVEN,
        compaction: config_update_params.Compaction | NotGiven = NOT_GIVEN,
        default_agent: str | NotGiven = NOT_GIVEN,
        disabled_providers: List[str] | NotGiven = NOT_GIVEN,
        enabled_providers: List[str] | NotGiven = NOT_GIVEN,
        enterprise: config_update_params.Enterprise | NotGiven = NOT_GIVEN,
        experimental: config_update_params.Experimental | NotGiven = NOT_GIVEN,
        formatter: bool | Dict[str, config_update_params.FormatterConfig] | NotGiven = NOT_GIVEN,
        instructions: List[str] | NotGiven = NOT_GIVEN,
        layout: Literal["auto", "stretch"] | NotGiven = NOT_GIVEN,
        log_level: Literal["DEBUG", "INFO", "WARN", "ERROR"] | NotGiven = NOT_GIVEN,
        lsp: bool | Dict[str, config_update_params.LspConfig] | NotGiven = NOT_GIVEN,
        mcp: Dict[str, config_update_params.Mcp] | NotGiven = NOT_GIVEN,
        mode: config_update_params.Mode | NotGiven = NOT_GIVEN,
        model: str | NotGiven = NOT_GIVEN,
        permission: config_update_params.PermissionConfig | NotGiven = NOT_GIVEN,
        plugin: List[Union[str, Tuple[str, object]]] | NotGiven = NOT_GIVEN,
        provider: config_update_params.Provider | NotGiven = NOT_GIVEN,
        reference: Dict[str, config_update_params.ReferenceConfigEntry] | NotGiven = NOT_GIVEN,
        server: config_update_params.Server | NotGiven = NOT_GIVEN,
        share: Literal["manual", "auto", "disabled"] | NotGiven = NOT_GIVEN,
        shell: str | NotGiven = NOT_GIVEN,
        skills: config_update_params.Skills | NotGiven = NOT_GIVEN,
        small_model: str | NotGiven = NOT_GIVEN,
        snapshot: bool | NotGiven = NOT_GIVEN,
        subagent_depth: int | NotGiven = NOT_GIVEN,
        tool_output: config_update_params.ToolOutput | NotGiven = NOT_GIVEN,
        tools: Dict[str, bool] | NotGiven = NOT_GIVEN,
        username: str | NotGiven = NOT_GIVEN,
        watcher: config_update_params.Watcher | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Config:
        """
        Update global OpenCode configuration settings and preferences.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._patch(
            "/global/config",
            body=await async_maybe_transform(
                {
                    "schema_": schema_,
                    "agent": agent,
                    "attachment": attachment,
                    "autoshare": autoshare,
                    "autoupdate": autoupdate,
                    "command": command,
                    "compaction": compaction,
                    "default_agent": default_agent,
                    "disabled_providers": disabled_providers,
                    "enabled_providers": enabled_providers,
                    "enterprise": enterprise,
                    "experimental": experimental,
                    "formatter": formatter,
                    "instructions": instructions,
                    "layout": layout,
                    "log_level": log_level,
                    "lsp": lsp,
                    "mcp": mcp,
                    "mode": mode,
                    "model": model,
                    "permission": permission,
                    "plugin": plugin,
                    "provider": provider,
                    "reference": reference,
                    "server": server,
                    "share": share,
                    "shell": shell,
                    "skills": skills,
                    "small_model": small_model,
                    "snapshot": snapshot,
                    "subagent_depth": subagent_depth,
                    "tool_output": tool_output,
                    "tools": tools,
                    "username": username,
                    "watcher": watcher,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=Config,
        )


class AsyncGlobalResource(AsyncAPIResource):
    @cached_property
    def config(self) -> AsyncGlobalConfigResource:
        return AsyncGlobalConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGlobalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGlobalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGlobalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncGlobalResourceWithStreamingResponse(self)

    async def health(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalHealthResponse:
        """Get health"""
        return await self._get(
            "/global/health",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=GlobalHealthResponse,
        )

    async def event(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncStream[GlobalEventResponse]:
        """Get global events"""
        return await self._get(
            "/global/event",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=GlobalEventResponse,
            stream=True,
            stream_cls=AsyncStream[GlobalEventResponse],
        )

    async def dispose(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalDisposeResponse:
        """Dispose of the global server instance and free its resources."""
        return await self._post(
            "/global/dispose",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=GlobalDisposeResponse,
        )

    async def upgrade(
        self,
        *,
        target: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GlobalUpgradeResponse:
        """
        Upgrade the OpenCode server.

        Args:
          target: Version to upgrade to; when omitted, upgrades to the latest
              available version.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            GlobalUpgradeResponse,
            await self._post(
                "/global/upgrade",
                body=await async_maybe_transform(
                    {
                        "target": target,
                    },
                    global_upgrade_params.GlobalUpgradeParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                ),
                cast_to=cast(Any, GlobalUpgradeResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class GlobalResourceWithRawResponse:
    def __init__(self, global_: GlobalResource) -> None:
        self._global = global_

        self.config = GlobalConfigResourceWithRawResponse(global_.config)
        self.health = to_raw_response_wrapper(
            global_.health,
        )
        self.event = to_raw_response_wrapper(
            global_.event,
        )
        self.dispose = to_raw_response_wrapper(
            global_.dispose,
        )
        self.upgrade = to_raw_response_wrapper(
            global_.upgrade,
        )


class GlobalConfigResourceWithRawResponse:
    def __init__(self, global_config: GlobalConfigResource) -> None:
        self._global_config = global_config

        self.get = to_raw_response_wrapper(
            global_config.get,
        )
        self.update = to_raw_response_wrapper(
            global_config.update,
        )


class AsyncGlobalResourceWithRawResponse:
    def __init__(self, global_: AsyncGlobalResource) -> None:
        self._global = global_

        self.config = AsyncGlobalConfigResourceWithRawResponse(global_.config)
        self.health = async_to_raw_response_wrapper(
            global_.health,
        )
        self.event = async_to_raw_response_wrapper(
            global_.event,
        )
        self.dispose = async_to_raw_response_wrapper(
            global_.dispose,
        )
        self.upgrade = async_to_raw_response_wrapper(
            global_.upgrade,
        )


class AsyncGlobalConfigResourceWithRawResponse:
    def __init__(self, global_config: AsyncGlobalConfigResource) -> None:
        self._global_config = global_config

        self.get = async_to_raw_response_wrapper(
            global_config.get,
        )
        self.update = async_to_raw_response_wrapper(
            global_config.update,
        )


class GlobalResourceWithStreamingResponse:
    def __init__(self, global_: GlobalResource) -> None:
        self._global = global_

        self.config = GlobalConfigResourceWithStreamingResponse(global_.config)
        self.health = to_streamed_response_wrapper(
            global_.health,
        )
        self.event = to_streamed_response_wrapper(
            global_.event,
        )
        self.dispose = to_streamed_response_wrapper(
            global_.dispose,
        )
        self.upgrade = to_streamed_response_wrapper(
            global_.upgrade,
        )


class GlobalConfigResourceWithStreamingResponse:
    def __init__(self, global_config: GlobalConfigResource) -> None:
        self._global_config = global_config

        self.get = to_streamed_response_wrapper(
            global_config.get,
        )
        self.update = to_streamed_response_wrapper(
            global_config.update,
        )


class AsyncGlobalResourceWithStreamingResponse:
    def __init__(self, global_: AsyncGlobalResource) -> None:
        self._global = global_

        self.config = AsyncGlobalConfigResourceWithStreamingResponse(global_.config)
        self.health = async_to_streamed_response_wrapper(
            global_.health,
        )
        self.event = async_to_streamed_response_wrapper(
            global_.event,
        )
        self.dispose = async_to_streamed_response_wrapper(
            global_.dispose,
        )
        self.upgrade = async_to_streamed_response_wrapper(
            global_.upgrade,
        )


class AsyncGlobalConfigResourceWithStreamingResponse:
    def __init__(self, global_config: AsyncGlobalConfigResource) -> None:
        self._global_config = global_config

        self.get = async_to_streamed_response_wrapper(
            global_config.get,
        )
        self.update = async_to_streamed_response_wrapper(
            global_config.update,
        )
