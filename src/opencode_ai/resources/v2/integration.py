# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

from typing import Dict

import httpx

from ...types import (
    v2_location_query_params,
    v2_integration_connect_key_params,
    v2_integration_connect_oauth_params,
    v2_integration_attempt_complete_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from ...types.v2_location_query_params import V2Location
from ...types.v2_integration_get_response import V2IntegrationGetResponse
from ...types.v2_integration_list_response import V2IntegrationListResponse
from ...types.v2_integration_connect_oauth_response import V2IntegrationConnectOauthResponse
from ...types.v2_integration_attempt_status_response import V2IntegrationAttemptStatusResponse

__all__ = ["V2IntegrationResource", "AsyncV2IntegrationResource"]


class V2IntegrationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> V2IntegrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V2IntegrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2IntegrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return V2IntegrationResourceWithStreamingResponse(self)

    def attempt_cancel(
        self,
        attempt_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Cancel OAuth connection"""
        if not attempt_id:
            raise ValueError(f"Expected a non-empty value for `attempt_id` but received {attempt_id!r}")
        return self._delete(
            f"/api/integration/attempt/{attempt_id}",
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
            cast_to=NoneType,
        )

    def attempt_complete(
        self,
        attempt_id: str,
        *,
        code: str | NotGiven = NOT_GIVEN,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Complete OAuth connection"""
        if not attempt_id:
            raise ValueError(f"Expected a non-empty value for `attempt_id` but received {attempt_id!r}")
        return self._post(
            f"/api/integration/attempt/{attempt_id}/complete",
            body=maybe_transform(
                {
                    "code": code,
                },
                v2_integration_attempt_complete_params.V2IntegrationAttemptCompleteParams,
            ),
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
            cast_to=NoneType,
        )

    def attempt_status(
        self,
        attempt_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2IntegrationAttemptStatusResponse:
        """Get OAuth attempt status"""
        if not attempt_id:
            raise ValueError(f"Expected a non-empty value for `attempt_id` but received {attempt_id!r}")
        return self._get(
            f"/api/integration/attempt/{attempt_id}",
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
            cast_to=V2IntegrationAttemptStatusResponse,
        )

    def connect_key(
        self,
        integration_id: str,
        *,
        key: str,
        label: str | NotGiven = NOT_GIVEN,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Connect with key"""
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._post(
            f"/api/integration/{integration_id}/connect/key",
            body=maybe_transform(
                {
                    "key": key,
                    "label": label,
                },
                v2_integration_connect_key_params.V2IntegrationConnectKeyParams,
            ),
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
            cast_to=NoneType,
        )

    def connect_oauth(
        self,
        integration_id: str,
        *,
        method_id: str,
        inputs: Dict[str, object],
        label: str | NotGiven = NOT_GIVEN,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2IntegrationConnectOauthResponse:
        """Begin OAuth connection"""
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._post(
            f"/api/integration/{integration_id}/connect/oauth",
            body=maybe_transform(
                {
                    "method_id": method_id,
                    "inputs": inputs,
                    "label": label,
                },
                v2_integration_connect_oauth_params.V2IntegrationConnectOauthParams,
            ),
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
            cast_to=V2IntegrationConnectOauthResponse,
        )

    def get(
        self,
        integration_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2IntegrationGetResponse:
        """Get integration"""
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return self._get(
            f"/api/integration/{integration_id}",
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
            cast_to=V2IntegrationGetResponse,
        )

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
    ) -> V2IntegrationListResponse:
        """List integrations"""
        return self._get(
            "/api/integration",
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
            cast_to=V2IntegrationListResponse,
        )


class AsyncV2IntegrationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncV2IntegrationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2IntegrationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2IntegrationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncV2IntegrationResourceWithStreamingResponse(self)

    async def attempt_cancel(
        self,
        attempt_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Cancel OAuth connection"""
        if not attempt_id:
            raise ValueError(f"Expected a non-empty value for `attempt_id` but received {attempt_id!r}")
        return await self._delete(
            f"/api/integration/attempt/{attempt_id}",
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
            cast_to=NoneType,
        )

    async def attempt_complete(
        self,
        attempt_id: str,
        *,
        code: str | NotGiven = NOT_GIVEN,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Complete OAuth connection"""
        if not attempt_id:
            raise ValueError(f"Expected a non-empty value for `attempt_id` but received {attempt_id!r}")
        return await self._post(
            f"/api/integration/attempt/{attempt_id}/complete",
            body=await async_maybe_transform(
                {
                    "code": code,
                },
                v2_integration_attempt_complete_params.V2IntegrationAttemptCompleteParams,
            ),
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
            cast_to=NoneType,
        )

    async def attempt_status(
        self,
        attempt_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2IntegrationAttemptStatusResponse:
        """Get OAuth attempt status"""
        if not attempt_id:
            raise ValueError(f"Expected a non-empty value for `attempt_id` but received {attempt_id!r}")
        return await self._get(
            f"/api/integration/attempt/{attempt_id}",
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
            cast_to=V2IntegrationAttemptStatusResponse,
        )

    async def connect_key(
        self,
        integration_id: str,
        *,
        key: str,
        label: str | NotGiven = NOT_GIVEN,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Connect with key"""
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._post(
            f"/api/integration/{integration_id}/connect/key",
            body=await async_maybe_transform(
                {
                    "key": key,
                    "label": label,
                },
                v2_integration_connect_key_params.V2IntegrationConnectKeyParams,
            ),
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
            cast_to=NoneType,
        )

    async def connect_oauth(
        self,
        integration_id: str,
        *,
        method_id: str,
        inputs: Dict[str, object],
        label: str | NotGiven = NOT_GIVEN,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2IntegrationConnectOauthResponse:
        """Begin OAuth connection"""
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._post(
            f"/api/integration/{integration_id}/connect/oauth",
            body=await async_maybe_transform(
                {
                    "method_id": method_id,
                    "inputs": inputs,
                    "label": label,
                },
                v2_integration_connect_oauth_params.V2IntegrationConnectOauthParams,
            ),
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
            cast_to=V2IntegrationConnectOauthResponse,
        )

    async def get(
        self,
        integration_id: str,
        *,
        location: V2Location | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> V2IntegrationGetResponse:
        """Get integration"""
        if not integration_id:
            raise ValueError(f"Expected a non-empty value for `integration_id` but received {integration_id!r}")
        return await self._get(
            f"/api/integration/{integration_id}",
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
            cast_to=V2IntegrationGetResponse,
        )

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
    ) -> V2IntegrationListResponse:
        """List integrations"""
        return await self._get(
            "/api/integration",
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
            cast_to=V2IntegrationListResponse,
        )


class V2IntegrationResourceWithRawResponse:
    def __init__(self, integration: V2IntegrationResource) -> None:
        self._integration = integration

        self.attempt_cancel = to_raw_response_wrapper(
            integration.attempt_cancel,
        )
        self.attempt_complete = to_raw_response_wrapper(
            integration.attempt_complete,
        )
        self.attempt_status = to_raw_response_wrapper(
            integration.attempt_status,
        )
        self.connect_key = to_raw_response_wrapper(
            integration.connect_key,
        )
        self.connect_oauth = to_raw_response_wrapper(
            integration.connect_oauth,
        )
        self.get = to_raw_response_wrapper(
            integration.get,
        )
        self.list = to_raw_response_wrapper(
            integration.list,
        )


class AsyncV2IntegrationResourceWithRawResponse:
    def __init__(self, integration: AsyncV2IntegrationResource) -> None:
        self._integration = integration

        self.attempt_cancel = async_to_raw_response_wrapper(
            integration.attempt_cancel,
        )
        self.attempt_complete = async_to_raw_response_wrapper(
            integration.attempt_complete,
        )
        self.attempt_status = async_to_raw_response_wrapper(
            integration.attempt_status,
        )
        self.connect_key = async_to_raw_response_wrapper(
            integration.connect_key,
        )
        self.connect_oauth = async_to_raw_response_wrapper(
            integration.connect_oauth,
        )
        self.get = async_to_raw_response_wrapper(
            integration.get,
        )
        self.list = async_to_raw_response_wrapper(
            integration.list,
        )


class V2IntegrationResourceWithStreamingResponse:
    def __init__(self, integration: V2IntegrationResource) -> None:
        self._integration = integration

        self.attempt_cancel = to_streamed_response_wrapper(
            integration.attempt_cancel,
        )
        self.attempt_complete = to_streamed_response_wrapper(
            integration.attempt_complete,
        )
        self.attempt_status = to_streamed_response_wrapper(
            integration.attempt_status,
        )
        self.connect_key = to_streamed_response_wrapper(
            integration.connect_key,
        )
        self.connect_oauth = to_streamed_response_wrapper(
            integration.connect_oauth,
        )
        self.get = to_streamed_response_wrapper(
            integration.get,
        )
        self.list = to_streamed_response_wrapper(
            integration.list,
        )


class AsyncV2IntegrationResourceWithStreamingResponse:
    def __init__(self, integration: AsyncV2IntegrationResource) -> None:
        self._integration = integration

        self.attempt_cancel = async_to_streamed_response_wrapper(
            integration.attempt_cancel,
        )
        self.attempt_complete = async_to_streamed_response_wrapper(
            integration.attempt_complete,
        )
        self.attempt_status = async_to_streamed_response_wrapper(
            integration.attempt_status,
        )
        self.connect_key = async_to_streamed_response_wrapper(
            integration.connect_key,
        )
        self.connect_oauth = async_to_streamed_response_wrapper(
            integration.connect_oauth,
        )
        self.get = async_to_streamed_response_wrapper(
            integration.get,
        )
        self.list = async_to_streamed_response_wrapper(
            integration.list,
        )
