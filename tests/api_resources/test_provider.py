# Hand-maintained fork of the Stainless-era opencode SDK. Generated code was replaced by manual maintenance; see CONTRIBUTING.md.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types import (
    ProviderAuthResponse,
    ProviderListResponse,
    ProviderAuthAuthorization,
    ProviderOAuthCallbackResponse,
)
from tests.wire_helpers import route_request, read_json_body

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

PROVIDER_SAMPLE: dict[str, object] = {
    "id": "anthropic",
    "name": "Anthropic",
    "source": "env",
    "env": ["ANTHROPIC_API_KEY"],
    "options": {},
    "models": {},
}

AUTH_METHOD_SAMPLE: dict[str, object] = {
    "type": "oauth",
    "label": "Anthropic OAuth",
}

AUTHORIZATION_SAMPLE: dict[str, object] = {
    "url": "https://example.com/authorize",
    "method": "auto",
    "instructions": "Follow the link to authorize.",
}


class TestProvider:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Opencode) -> None:
        provider = client.provider.list()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Opencode) -> None:
        response = client.provider.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Opencode) -> None:
        with client.provider.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(ProviderListResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_auth(self, client: Opencode) -> None:
        provider = client.provider.auth()
        assert_matches_type(ProviderAuthResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_auth(self, client: Opencode) -> None:
        response = client.provider.with_raw_response.auth()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(ProviderAuthResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_auth(self, client: Opencode) -> None:
        with client.provider.with_streaming_response.auth() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(ProviderAuthResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_oauth_authorize(self, client: Opencode) -> None:
        provider = client.provider.oauth_authorize(
            provider_id="providerID",
            method=0,
        )
        assert_matches_type(ProviderAuthAuthorization, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_oauth_authorize_with_all_params(self, client: Opencode) -> None:
        provider = client.provider.oauth_authorize(
            provider_id="providerID",
            method=0,
            inputs={"foo": "bar"},
        )
        assert_matches_type(ProviderAuthAuthorization, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_oauth_authorize(self, client: Opencode) -> None:
        response = client.provider.with_raw_response.oauth_authorize(
            provider_id="providerID",
            method=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(ProviderAuthAuthorization, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_oauth_authorize(self, client: Opencode) -> None:
        with client.provider.with_streaming_response.oauth_authorize(
            provider_id="providerID",
            method=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(ProviderAuthAuthorization, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_oauth_authorize(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            client.provider.with_raw_response.oauth_authorize(
                provider_id="",
                method=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_oauth_callback(self, client: Opencode) -> None:
        provider = client.provider.oauth_callback(
            provider_id="providerID",
            method=0,
        )
        assert_matches_type(ProviderOAuthCallbackResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_oauth_callback_with_all_params(self, client: Opencode) -> None:
        provider = client.provider.oauth_callback(
            provider_id="providerID",
            method=0,
            code="code",
        )
        assert_matches_type(ProviderOAuthCallbackResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_oauth_callback(self, client: Opencode) -> None:
        response = client.provider.with_raw_response.oauth_callback(
            provider_id="providerID",
            method=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = response.parse()
        assert_matches_type(ProviderOAuthCallbackResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_oauth_callback(self, client: Opencode) -> None:
        with client.provider.with_streaming_response.oauth_callback(
            provider_id="providerID",
            method=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = response.parse()
            assert_matches_type(ProviderOAuthCallbackResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_oauth_callback(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            client.provider.with_raw_response.oauth_callback(
                provider_id="",
                method=0,
            )


class TestProviderWire:
    @pytest.mark.respx(base_url=base_url)
    def test_list_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/provider").mock(
            return_value=httpx.Response(
                200,
                json={"all": [PROVIDER_SAMPLE], "default": {"anthropic": "claude"}, "connected": ["anthropic"]},
            )
        )
        result = client.provider.list()
        assert route.called
        assert route.calls.last.request.method == "GET"
        assert_matches_type(ProviderListResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_auth_wire_shape(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/provider/auth").mock(
            return_value=httpx.Response(200, json={"anthropic": [AUTH_METHOD_SAMPLE]})
        )
        result = client.provider.auth()
        assert route.called
        assert route.calls.last.request.method == "GET"
        assert_matches_type(ProviderAuthResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_oauth_authorize_sends_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/provider/anthropic/oauth/authorize").mock(
            return_value=httpx.Response(200, json=AUTHORIZATION_SAMPLE)
        )
        result = client.provider.oauth_authorize(
            provider_id="anthropic",
            method=1,
            inputs={"apiKey": "sk-test"},
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body == {"method": 1, "inputs": {"apiKey": "sk-test"}}
        assert_matches_type(ProviderAuthAuthorization, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    def test_oauth_callback_sends_body(self, client: Opencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/provider/anthropic/oauth/callback").mock(return_value=httpx.Response(200, json=True))
        result = client.provider.oauth_callback(
            provider_id="anthropic",
            method=1,
            code="the-code",
        )
        assert route.called
        request = route_request(route)
        assert request.method == "POST"
        body = read_json_body(route)
        assert body == {"method": 1, "code": "the-code"}
        assert_matches_type(ProviderOAuthCallbackResponse, result, path=["response"])


class TestAsyncProvider:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncOpencode) -> None:
        provider = await async_client.provider.list()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpencode) -> None:
        response = await async_client.provider.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(ProviderListResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpencode) -> None:
        async with async_client.provider.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(ProviderListResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_auth(self, async_client: AsyncOpencode) -> None:
        provider = await async_client.provider.auth()
        assert_matches_type(ProviderAuthResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_auth(self, async_client: AsyncOpencode) -> None:
        response = await async_client.provider.with_raw_response.auth()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(ProviderAuthResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_auth(self, async_client: AsyncOpencode) -> None:
        async with async_client.provider.with_streaming_response.auth() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(ProviderAuthResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_oauth_authorize(self, async_client: AsyncOpencode) -> None:
        provider = await async_client.provider.oauth_authorize(
            provider_id="providerID",
            method=0,
        )
        assert_matches_type(ProviderAuthAuthorization, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_oauth_authorize_with_all_params(self, async_client: AsyncOpencode) -> None:
        provider = await async_client.provider.oauth_authorize(
            provider_id="providerID",
            method=0,
            inputs={"foo": "bar"},
        )
        assert_matches_type(ProviderAuthAuthorization, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_oauth_authorize(self, async_client: AsyncOpencode) -> None:
        response = await async_client.provider.with_raw_response.oauth_authorize(
            provider_id="providerID",
            method=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(ProviderAuthAuthorization, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_oauth_authorize(self, async_client: AsyncOpencode) -> None:
        async with async_client.provider.with_streaming_response.oauth_authorize(
            provider_id="providerID",
            method=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(ProviderAuthAuthorization, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_oauth_authorize(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            await async_client.provider.with_raw_response.oauth_authorize(
                provider_id="",
                method=0,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_oauth_callback(self, async_client: AsyncOpencode) -> None:
        provider = await async_client.provider.oauth_callback(
            provider_id="providerID",
            method=0,
        )
        assert_matches_type(ProviderOAuthCallbackResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_oauth_callback_with_all_params(self, async_client: AsyncOpencode) -> None:
        provider = await async_client.provider.oauth_callback(
            provider_id="providerID",
            method=0,
            code="code",
        )
        assert_matches_type(ProviderOAuthCallbackResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_oauth_callback(self, async_client: AsyncOpencode) -> None:
        response = await async_client.provider.with_raw_response.oauth_callback(
            provider_id="providerID",
            method=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        provider = await response.parse()
        assert_matches_type(ProviderOAuthCallbackResponse, provider, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_oauth_callback(self, async_client: AsyncOpencode) -> None:
        async with async_client.provider.with_streaming_response.oauth_callback(
            provider_id="providerID",
            method=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            provider = await response.parse()
            assert_matches_type(ProviderOAuthCallbackResponse, provider, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_oauth_callback(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider_id` but received ''"):
            await async_client.provider.with_raw_response.oauth_callback(
                provider_id="",
                method=0,
            )


class TestAsyncProviderWire:
    @pytest.mark.respx(base_url=base_url)
    async def test_list_wire_shape(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.get("/provider").mock(
            return_value=httpx.Response(
                200,
                json={"all": [PROVIDER_SAMPLE], "default": {"anthropic": "claude"}, "connected": ["anthropic"]},
            )
        )
        result = await async_client.provider.list()
        assert route.called
        assert route.calls.last.request.method == "GET"
        assert_matches_type(ProviderListResponse, result, path=["response"])

    @pytest.mark.respx(base_url=base_url)
    async def test_oauth_callback_sends_body(self, async_client: AsyncOpencode, respx_mock: MockRouter) -> None:
        route = respx_mock.post("/provider/anthropic/oauth/callback").mock(return_value=httpx.Response(200, json=False))
        result = await async_client.provider.oauth_callback(
            provider_id="anthropic",
            method=1,
        )
        assert route.called
        body = read_json_body(route)
        assert body == {"method": 1}
        assert_matches_type(ProviderOAuthCallbackResponse, result, path=["response"])
