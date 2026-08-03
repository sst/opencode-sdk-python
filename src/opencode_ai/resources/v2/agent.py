# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import httpx

from ...types import v2_location_query_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.v2_agent_list_response import V2AgentListResponse
from ...types.v2_location_query_params import V2Location

__all__ = ["V2AgentResource", "AsyncV2AgentResource"]


class V2AgentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2AgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V2AgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2AgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return V2AgentResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2AgentListResponse:
        """List agents"""
        return self._get(
            "/api/agent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"location": location},
                    v2_location_query_params.V2LocationQueryParams,
                ),
            ),
            cast_to=V2AgentListResponse,
        )


class AsyncV2AgentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2AgentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2AgentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2AgentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncV2AgentResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2AgentListResponse:
        """List agents"""
        return await self._get(
            "/api/agent",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"location": location},
                    v2_location_query_params.V2LocationQueryParams,
                ),
            ),
            cast_to=V2AgentListResponse,
        )


class V2AgentResourceWithRawResponse:
    def __init__(self, agent: V2AgentResource) -> None:
        self._agent = agent

        self.list = to_raw_response_wrapper(
            agent.list,
        )


class AsyncV2AgentResourceWithRawResponse:
    def __init__(self, agent: AsyncV2AgentResource) -> None:
        self._agent = agent

        self.list = async_to_raw_response_wrapper(
            agent.list,
        )


class V2AgentResourceWithStreamingResponse:
    def __init__(self, agent: V2AgentResource) -> None:
        self._agent = agent

        self.list = to_streamed_response_wrapper(
            agent.list,
        )


class AsyncV2AgentResourceWithStreamingResponse:
    def __init__(self, agent: AsyncV2AgentResource) -> None:
        self._agent = agent

        self.list = async_to_streamed_response_wrapper(
            agent.list,
        )
