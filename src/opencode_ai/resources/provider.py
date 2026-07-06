# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..types import provider_oauth_callback_params, provider_oauth_authorize_params
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
from ..types.provider_auth_response import ProviderAuthResponse
from ..types.provider_list_response import ProviderListResponse
from ..types.provider_auth_authorization import ProviderAuthAuthorization
from ..types.provider_oauth_callback_response import ProviderOAuthCallbackResponse

__all__ = ["ProviderResource", "AsyncProviderResource"]


class ProviderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProviderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return ProviderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProviderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return ProviderResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderListResponse:
        """Get a list of all available AI providers, including both available and
        connected ones."""
        return self._get(
            "/provider",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderListResponse,
        )

    def auth(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderAuthResponse:
        """Retrieve available authentication methods for all AI providers."""
        return self._get(
            "/provider/auth",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderAuthResponse,
        )

    def oauth_authorize(
        self,
        provider_id: str,
        *,
        method: float,
        inputs: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderAuthAuthorization:
        """
        Start the OAuth authorization flow for a provider.

        Args:
          method: Auth method index

              Note: this is unrelated to the `method` field on the response
              (`ProviderAuthAuthorization.method`), which is a string enum
              (`"auto" | "code"`) describing how the returned URL should be
              handled, not a request-selecting index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return self._post(
            f"/provider/{provider_id}/oauth/authorize",
            body=maybe_transform(
                {
                    "method": method,
                    "inputs": inputs,
                },
                provider_oauth_authorize_params.ProviderOAuthAuthorizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderAuthAuthorization,
        )

    def oauth_callback(
        self,
        provider_id: str,
        *,
        method: float,
        code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderOAuthCallbackResponse:
        """
        Handle the OAuth callback from a provider after user authorization.

        Args:
          method: Auth method index

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return self._post(
            f"/provider/{provider_id}/oauth/callback",
            body=maybe_transform(
                {
                    "method": method,
                    "code": code,
                },
                provider_oauth_callback_params.ProviderOAuthCallbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderOAuthCallbackResponse,
        )


class AsyncProviderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProviderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/sst/opencode-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProviderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProviderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/sst/opencode-sdk-python#with_streaming_response
        """
        return AsyncProviderResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderListResponse:
        """Get a list of all available AI providers, including both available and
        connected ones."""
        return await self._get(
            "/provider",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderListResponse,
        )

    async def auth(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderAuthResponse:
        """Retrieve available authentication methods for all AI providers."""
        return await self._get(
            "/provider/auth",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderAuthResponse,
        )

    async def oauth_authorize(
        self,
        provider_id: str,
        *,
        method: float,
        inputs: Dict[str, str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderAuthAuthorization:
        """
        Start the OAuth authorization flow for a provider.

        Args:
          method: Auth method index

              Note: this is unrelated to the `method` field on the response
              (`ProviderAuthAuthorization.method`), which is a string enum
              (`"auto" | "code"`) describing how the returned URL should be
              handled, not a request-selecting index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return await self._post(
            f"/provider/{provider_id}/oauth/authorize",
            body=await async_maybe_transform(
                {
                    "method": method,
                    "inputs": inputs,
                },
                provider_oauth_authorize_params.ProviderOAuthAuthorizeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderAuthAuthorization,
        )

    async def oauth_callback(
        self,
        provider_id: str,
        *,
        method: float,
        code: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ProviderOAuthCallbackResponse:
        """
        Handle the OAuth callback from a provider after user authorization.

        Args:
          method: Auth method index

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not provider_id:
            raise ValueError(f"Expected a non-empty value for `provider_id` but received {provider_id!r}")
        return await self._post(
            f"/provider/{provider_id}/oauth/callback",
            body=await async_maybe_transform(
                {
                    "method": method,
                    "code": code,
                },
                provider_oauth_callback_params.ProviderOAuthCallbackParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProviderOAuthCallbackResponse,
        )


class ProviderResourceWithRawResponse:
    def __init__(self, provider: ProviderResource) -> None:
        self._provider = provider

        self.list = to_raw_response_wrapper(
            provider.list,
        )
        self.auth = to_raw_response_wrapper(
            provider.auth,
        )
        self.oauth_authorize = to_raw_response_wrapper(
            provider.oauth_authorize,
        )
        self.oauth_callback = to_raw_response_wrapper(
            provider.oauth_callback,
        )


class AsyncProviderResourceWithRawResponse:
    def __init__(self, provider: AsyncProviderResource) -> None:
        self._provider = provider

        self.list = async_to_raw_response_wrapper(
            provider.list,
        )
        self.auth = async_to_raw_response_wrapper(
            provider.auth,
        )
        self.oauth_authorize = async_to_raw_response_wrapper(
            provider.oauth_authorize,
        )
        self.oauth_callback = async_to_raw_response_wrapper(
            provider.oauth_callback,
        )


class ProviderResourceWithStreamingResponse:
    def __init__(self, provider: ProviderResource) -> None:
        self._provider = provider

        self.list = to_streamed_response_wrapper(
            provider.list,
        )
        self.auth = to_streamed_response_wrapper(
            provider.auth,
        )
        self.oauth_authorize = to_streamed_response_wrapper(
            provider.oauth_authorize,
        )
        self.oauth_callback = to_streamed_response_wrapper(
            provider.oauth_callback,
        )


class AsyncProviderResourceWithStreamingResponse:
    def __init__(self, provider: AsyncProviderResource) -> None:
        self._provider = provider

        self.list = async_to_streamed_response_wrapper(
            provider.list,
        )
        self.auth = async_to_streamed_response_wrapper(
            provider.auth,
        )
        self.oauth_authorize = async_to_streamed_response_wrapper(
            provider.oauth_authorize,
        )
        self.oauth_callback = async_to_streamed_response_wrapper(
            provider.oauth_callback,
        )
