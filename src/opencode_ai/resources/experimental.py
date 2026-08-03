# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import httpx

from ..types import (
    addressing_params,
    experimental_session_list_params,
    experimental_workspace_warp_params,
    experimental_workspace_create_params,
    experimental_console_switch_org_params,
    experimental_control_plane_move_session_params,
    experimental_project_copy_generate_name_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ..types.experimental_console_get_response import ConsoleState
from ..types.experimental_capabilities_response import ExperimentalCapabilitiesResponse
from ..types.experimental_session_list_response import ExperimentalSessionListResponse
from ..types.experimental_resource_list_response import ExperimentalResourceListResponse
from ..types.experimental_workspace_list_response import ExperimentalWorkspaceListResponse
from ..types.experimental_workspace_create_response import ExperimentalWorkspaceCreateResponse
from ..types.experimental_workspace_remove_response import ExperimentalWorkspaceRemoveResponse
from ..types.experimental_workspace_status_response import ExperimentalWorkspaceStatusResponse
from ..types.experimental_console_list_orgs_response import ExperimentalConsoleListOrgsResponse
from ..types.experimental_console_switch_org_response import ExperimentalConsoleSwitchOrgResponse
from ..types.experimental_session_background_response import ExperimentalSessionBackgroundResponse
from ..types.experimental_workspace_adapter_list_response import ExperimentalWorkspaceAdapterListResponse
from ..types.experimental_project_copy_generate_name_response import ExperimentalProjectCopyGenerateNameResponse

__all__ = ["ExperimentalResource", "AsyncExperimentalResource"]


class ExperimentalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExperimentalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ExperimentalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExperimentalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return ExperimentalResourceWithStreamingResponse(self)

    def capabilities_get(
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
    ) -> ExperimentalCapabilitiesResponse:
        """
        Get the capabilities of the experimental API
        """
        return self._get(
            "/experimental/capabilities",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalCapabilitiesResponse,
        )

    def console_get(
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
    ) -> ConsoleState:
        """
        Get the current console state
        """
        return self._get(
            "/experimental/console",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ConsoleState,
        )

    def console_list_orgs(
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
    ) -> ExperimentalConsoleListOrgsResponse:
        """
        List the Console orgs available to switch to
        """
        return self._get(
            "/experimental/console/orgs",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalConsoleListOrgsResponse,
        )

    def console_switch_org(
        self,
        *,
        account_id: str,
        org_id: str,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentalConsoleSwitchOrgResponse:
        """
        Switch the Console org
        """
        return self._post(
            "/experimental/console/switch",
            body=maybe_transform(
                {
                    "account_id": account_id,
                    "org_id": org_id,
                },
                experimental_console_switch_org_params.ExperimentalConsoleSwitchOrgParams,
            ),
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalConsoleSwitchOrgResponse,
        )

    def session_list(
        self,
        *,
        roots: bool | NotGiven = NOT_GIVEN,
        start: float | NotGiven = NOT_GIVEN,
        cursor: float | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        archived: bool | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentalSessionListResponse:
        """
        List sessions across all projects
        """
        return self._get(
            "/experimental/session",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "roots": roots,
                        "start": start,
                        "cursor": cursor,
                        "search": search,
                        "limit": limit,
                        "archived": archived,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    experimental_session_list_params.ExperimentalSessionListParams,
                ),
            ),
            cast_to=ExperimentalSessionListResponse,
        )

    def session_background(
        self,
        session_id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentalSessionBackgroundResponse:
        """
        Background a session's subagents
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return self._post(
            f"/experimental/session/{session_id}/background",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalSessionBackgroundResponse,
        )

    def resource_list(
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
    ) -> ExperimentalResourceListResponse:
        """
        List MCP resources
        """
        return self._get(
            "/experimental/resource",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalResourceListResponse,
        )

    def control_plane_move_session(
        self,
        *,
        session_id: str,
        destination: experimental_control_plane_move_session_params.MoveSessionDestination,
        move_changes: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Move a session to another directory
        """
        return self._post(
            "/experimental/control-plane/move-session",
            body=maybe_transform(
                {
                    "session_id": session_id,
                    "destination": destination,
                    "move_changes": move_changes,
                },
                experimental_control_plane_move_session_params.ExperimentalControlPlaneMoveSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    def project_copy_generate_name(
        self,
        project_id: str,
        *,
        context: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentalProjectCopyGenerateNameResponse:
        """
        Generate a name for a project copy
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return self._post(
            f"/experimental/project/{project_id}/copy/generate-name",
            body=maybe_transform(
                {
                    "context": context,
                },
                experimental_project_copy_generate_name_params.ExperimentalProjectCopyGenerateNameParams,
            ),
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalProjectCopyGenerateNameResponse,
        )

    def workspace_list(
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
    ) -> ExperimentalWorkspaceListResponse:
        """
        List workspaces
        """
        return self._get(
            "/experimental/workspace",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalWorkspaceListResponse,
        )

    def workspace_create(
        self,
        *,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        branch: str | NotGiven = NOT_GIVEN,
        extra: object | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentalWorkspaceCreateResponse:
        """
        Create a workspace
        """
        return self._post(
            "/experimental/workspace",
            body=maybe_transform(
                {
                    "type": type,
                    "id": id,
                    "branch": branch,
                    "extra": extra,
                },
                experimental_workspace_create_params.ExperimentalWorkspaceCreateParams,
            ),
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalWorkspaceCreateResponse,
        )

    def workspace_sync_list(
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
    ) -> None:
        """
        Sync the workspace list
        """
        return self._post(
            "/experimental/workspace/sync-list",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=NoneType,
        )

    def workspace_status(
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
    ) -> ExperimentalWorkspaceStatusResponse:
        """
        Get the status of all workspaces
        """
        return self._get(
            "/experimental/workspace/status",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalWorkspaceStatusResponse,
        )

    def workspace_remove(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentalWorkspaceRemoveResponse:
        """
        Remove a workspace
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/experimental/workspace/{id}",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalWorkspaceRemoveResponse,
        )

    def workspace_warp(
        self,
        *,
        id: str | None,
        session_id: str,
        copy_changes: bool | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Warp a session to a workspace
        """
        return self._post(
            "/experimental/workspace/warp",
            body=maybe_transform(
                {
                    "id": id,
                    "session_id": session_id,
                    "copy_changes": copy_changes,
                },
                experimental_workspace_warp_params.ExperimentalWorkspaceWarpParams,
            ),
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=NoneType,
        )

    def workspace_adapter_list(
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
    ) -> ExperimentalWorkspaceAdapterListResponse:
        """
        List the available workspace adapters
        """
        return self._get(
            "/experimental/workspace/adapter",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalWorkspaceAdapterListResponse,
        )


class AsyncExperimentalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExperimentalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExperimentalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExperimentalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncExperimentalResourceWithStreamingResponse(self)

    async def capabilities_get(
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
    ) -> ExperimentalCapabilitiesResponse:
        """
        Get the capabilities of the experimental API
        """
        return await self._get(
            "/experimental/capabilities",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalCapabilitiesResponse,
        )

    async def console_get(
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
    ) -> ConsoleState:
        """
        Get the current console state
        """
        return await self._get(
            "/experimental/console",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ConsoleState,
        )

    async def console_list_orgs(
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
    ) -> ExperimentalConsoleListOrgsResponse:
        """
        List the Console orgs available to switch to
        """
        return await self._get(
            "/experimental/console/orgs",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalConsoleListOrgsResponse,
        )

    async def console_switch_org(
        self,
        *,
        account_id: str,
        org_id: str,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentalConsoleSwitchOrgResponse:
        """
        Switch the Console org
        """
        return await self._post(
            "/experimental/console/switch",
            body=await async_maybe_transform(
                {
                    "account_id": account_id,
                    "org_id": org_id,
                },
                experimental_console_switch_org_params.ExperimentalConsoleSwitchOrgParams,
            ),
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalConsoleSwitchOrgResponse,
        )

    async def session_list(
        self,
        *,
        roots: bool | NotGiven = NOT_GIVEN,
        start: float | NotGiven = NOT_GIVEN,
        cursor: float | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        limit: float | NotGiven = NOT_GIVEN,
        archived: bool | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentalSessionListResponse:
        """
        List sessions across all projects
        """
        return await self._get(
            "/experimental/session",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "roots": roots,
                        "start": start,
                        "cursor": cursor,
                        "search": search,
                        "limit": limit,
                        "archived": archived,
                        "directory": directory,
                        "workspace": workspace,
                    },
                    experimental_session_list_params.ExperimentalSessionListParams,
                ),
            ),
            cast_to=ExperimentalSessionListResponse,
        )

    async def session_background(
        self,
        session_id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentalSessionBackgroundResponse:
        """
        Background a session's subagents
        """
        if not session_id:
            raise ValueError(f"Expected a non-empty value for `session_id` but received {session_id!r}")
        return await self._post(
            f"/experimental/session/{session_id}/background",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalSessionBackgroundResponse,
        )

    async def resource_list(
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
    ) -> ExperimentalResourceListResponse:
        """
        List MCP resources
        """
        return await self._get(
            "/experimental/resource",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalResourceListResponse,
        )

    async def control_plane_move_session(
        self,
        *,
        session_id: str,
        destination: experimental_control_plane_move_session_params.MoveSessionDestination,
        move_changes: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Move a session to another directory
        """
        return await self._post(
            "/experimental/control-plane/move-session",
            body=await async_maybe_transform(
                {
                    "session_id": session_id,
                    "destination": destination,
                    "move_changes": move_changes,
                },
                experimental_control_plane_move_session_params.ExperimentalControlPlaneMoveSessionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=NoneType,
        )

    async def project_copy_generate_name(
        self,
        project_id: str,
        *,
        context: str | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentalProjectCopyGenerateNameResponse:
        """
        Generate a name for a project copy
        """
        if not project_id:
            raise ValueError(f"Expected a non-empty value for `project_id` but received {project_id!r}")
        return await self._post(
            f"/experimental/project/{project_id}/copy/generate-name",
            body=await async_maybe_transform(
                {
                    "context": context,
                },
                experimental_project_copy_generate_name_params.ExperimentalProjectCopyGenerateNameParams,
            ),
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalProjectCopyGenerateNameResponse,
        )

    async def workspace_list(
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
    ) -> ExperimentalWorkspaceListResponse:
        """
        List workspaces
        """
        return await self._get(
            "/experimental/workspace",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalWorkspaceListResponse,
        )

    async def workspace_create(
        self,
        *,
        type: str,
        id: str | NotGiven = NOT_GIVEN,
        branch: str | NotGiven = NOT_GIVEN,
        extra: object | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentalWorkspaceCreateResponse:
        """
        Create a workspace
        """
        return await self._post(
            "/experimental/workspace",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "id": id,
                    "branch": branch,
                    "extra": extra,
                },
                experimental_workspace_create_params.ExperimentalWorkspaceCreateParams,
            ),
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalWorkspaceCreateResponse,
        )

    async def workspace_sync_list(
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
    ) -> None:
        """
        Sync the workspace list
        """
        return await self._post(
            "/experimental/workspace/sync-list",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def workspace_status(
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
    ) -> ExperimentalWorkspaceStatusResponse:
        """
        Get the status of all workspaces
        """
        return await self._get(
            "/experimental/workspace/status",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalWorkspaceStatusResponse,
        )

    async def workspace_remove(
        self,
        id: str,
        *,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ExperimentalWorkspaceRemoveResponse:
        """
        Remove a workspace
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/experimental/workspace/{id}",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalWorkspaceRemoveResponse,
        )

    async def workspace_warp(
        self,
        *,
        id: str | None,
        session_id: str,
        copy_changes: bool | NotGiven = NOT_GIVEN,
        directory: str | NotGiven = NOT_GIVEN,
        workspace: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Warp a session to a workspace
        """
        return await self._post(
            "/experimental/workspace/warp",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "session_id": session_id,
                    "copy_changes": copy_changes,
                },
                experimental_workspace_warp_params.ExperimentalWorkspaceWarpParams,
            ),
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=NoneType,
        )

    async def workspace_adapter_list(
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
    ) -> ExperimentalWorkspaceAdapterListResponse:
        """
        List the available workspace adapters
        """
        return await self._get(
            "/experimental/workspace/adapter",
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
                    addressing_params.AddressingParams,
                ),
            ),
            cast_to=ExperimentalWorkspaceAdapterListResponse,
        )


class ExperimentalResourceWithRawResponse:
    def __init__(self, experimental: ExperimentalResource) -> None:
        self._experimental = experimental

        self.capabilities_get = to_raw_response_wrapper(
            experimental.capabilities_get,
        )
        self.console_get = to_raw_response_wrapper(
            experimental.console_get,
        )
        self.console_list_orgs = to_raw_response_wrapper(
            experimental.console_list_orgs,
        )
        self.console_switch_org = to_raw_response_wrapper(
            experimental.console_switch_org,
        )
        self.session_list = to_raw_response_wrapper(
            experimental.session_list,
        )
        self.session_background = to_raw_response_wrapper(
            experimental.session_background,
        )
        self.resource_list = to_raw_response_wrapper(
            experimental.resource_list,
        )
        self.control_plane_move_session = to_raw_response_wrapper(
            experimental.control_plane_move_session,
        )
        self.project_copy_generate_name = to_raw_response_wrapper(
            experimental.project_copy_generate_name,
        )
        self.workspace_list = to_raw_response_wrapper(
            experimental.workspace_list,
        )
        self.workspace_create = to_raw_response_wrapper(
            experimental.workspace_create,
        )
        self.workspace_sync_list = to_raw_response_wrapper(
            experimental.workspace_sync_list,
        )
        self.workspace_status = to_raw_response_wrapper(
            experimental.workspace_status,
        )
        self.workspace_remove = to_raw_response_wrapper(
            experimental.workspace_remove,
        )
        self.workspace_warp = to_raw_response_wrapper(
            experimental.workspace_warp,
        )
        self.workspace_adapter_list = to_raw_response_wrapper(
            experimental.workspace_adapter_list,
        )


class AsyncExperimentalResourceWithRawResponse:
    def __init__(self, experimental: AsyncExperimentalResource) -> None:
        self._experimental = experimental

        self.capabilities_get = async_to_raw_response_wrapper(
            experimental.capabilities_get,
        )
        self.console_get = async_to_raw_response_wrapper(
            experimental.console_get,
        )
        self.console_list_orgs = async_to_raw_response_wrapper(
            experimental.console_list_orgs,
        )
        self.console_switch_org = async_to_raw_response_wrapper(
            experimental.console_switch_org,
        )
        self.session_list = async_to_raw_response_wrapper(
            experimental.session_list,
        )
        self.session_background = async_to_raw_response_wrapper(
            experimental.session_background,
        )
        self.resource_list = async_to_raw_response_wrapper(
            experimental.resource_list,
        )
        self.control_plane_move_session = async_to_raw_response_wrapper(
            experimental.control_plane_move_session,
        )
        self.project_copy_generate_name = async_to_raw_response_wrapper(
            experimental.project_copy_generate_name,
        )
        self.workspace_list = async_to_raw_response_wrapper(
            experimental.workspace_list,
        )
        self.workspace_create = async_to_raw_response_wrapper(
            experimental.workspace_create,
        )
        self.workspace_sync_list = async_to_raw_response_wrapper(
            experimental.workspace_sync_list,
        )
        self.workspace_status = async_to_raw_response_wrapper(
            experimental.workspace_status,
        )
        self.workspace_remove = async_to_raw_response_wrapper(
            experimental.workspace_remove,
        )
        self.workspace_warp = async_to_raw_response_wrapper(
            experimental.workspace_warp,
        )
        self.workspace_adapter_list = async_to_raw_response_wrapper(
            experimental.workspace_adapter_list,
        )


class ExperimentalResourceWithStreamingResponse:
    def __init__(self, experimental: ExperimentalResource) -> None:
        self._experimental = experimental

        self.capabilities_get = to_streamed_response_wrapper(
            experimental.capabilities_get,
        )
        self.console_get = to_streamed_response_wrapper(
            experimental.console_get,
        )
        self.console_list_orgs = to_streamed_response_wrapper(
            experimental.console_list_orgs,
        )
        self.console_switch_org = to_streamed_response_wrapper(
            experimental.console_switch_org,
        )
        self.session_list = to_streamed_response_wrapper(
            experimental.session_list,
        )
        self.session_background = to_streamed_response_wrapper(
            experimental.session_background,
        )
        self.resource_list = to_streamed_response_wrapper(
            experimental.resource_list,
        )
        self.control_plane_move_session = to_streamed_response_wrapper(
            experimental.control_plane_move_session,
        )
        self.project_copy_generate_name = to_streamed_response_wrapper(
            experimental.project_copy_generate_name,
        )
        self.workspace_list = to_streamed_response_wrapper(
            experimental.workspace_list,
        )
        self.workspace_create = to_streamed_response_wrapper(
            experimental.workspace_create,
        )
        self.workspace_sync_list = to_streamed_response_wrapper(
            experimental.workspace_sync_list,
        )
        self.workspace_status = to_streamed_response_wrapper(
            experimental.workspace_status,
        )
        self.workspace_remove = to_streamed_response_wrapper(
            experimental.workspace_remove,
        )
        self.workspace_warp = to_streamed_response_wrapper(
            experimental.workspace_warp,
        )
        self.workspace_adapter_list = to_streamed_response_wrapper(
            experimental.workspace_adapter_list,
        )


class AsyncExperimentalResourceWithStreamingResponse:
    def __init__(self, experimental: AsyncExperimentalResource) -> None:
        self._experimental = experimental

        self.capabilities_get = async_to_streamed_response_wrapper(
            experimental.capabilities_get,
        )
        self.console_get = async_to_streamed_response_wrapper(
            experimental.console_get,
        )
        self.console_list_orgs = async_to_streamed_response_wrapper(
            experimental.console_list_orgs,
        )
        self.console_switch_org = async_to_streamed_response_wrapper(
            experimental.console_switch_org,
        )
        self.session_list = async_to_streamed_response_wrapper(
            experimental.session_list,
        )
        self.session_background = async_to_streamed_response_wrapper(
            experimental.session_background,
        )
        self.resource_list = async_to_streamed_response_wrapper(
            experimental.resource_list,
        )
        self.control_plane_move_session = async_to_streamed_response_wrapper(
            experimental.control_plane_move_session,
        )
        self.project_copy_generate_name = async_to_streamed_response_wrapper(
            experimental.project_copy_generate_name,
        )
        self.workspace_list = async_to_streamed_response_wrapper(
            experimental.workspace_list,
        )
        self.workspace_create = async_to_streamed_response_wrapper(
            experimental.workspace_create,
        )
        self.workspace_sync_list = async_to_streamed_response_wrapper(
            experimental.workspace_sync_list,
        )
        self.workspace_status = async_to_streamed_response_wrapper(
            experimental.workspace_status,
        )
        self.workspace_remove = async_to_streamed_response_wrapper(
            experimental.workspace_remove,
        )
        self.workspace_warp = async_to_streamed_response_wrapper(
            experimental.workspace_warp,
        )
        self.workspace_adapter_list = async_to_streamed_response_wrapper(
            experimental.workspace_adapter_list,
        )
