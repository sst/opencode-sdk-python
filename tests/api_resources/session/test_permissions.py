# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from opencode_ai import Opencode, AsyncOpencode
from tests.utils import assert_matches_type
from opencode_ai.types.session import PermissionRespondResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPermissions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_respond(self, client: Opencode) -> None:
        permission = client.session.permissions.respond(
            permission_id="permissionID",
            id="id",
            response="once",
        )
        assert_matches_type(PermissionRespondResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_respond_with_all_params(self, client: Opencode) -> None:
        permission = client.session.permissions.respond(
            permission_id="permissionID",
            id="id",
            response="once",
            directory="directory",
        )
        assert_matches_type(PermissionRespondResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_respond(self, client: Opencode) -> None:
        response = client.session.permissions.with_raw_response.respond(
            permission_id="permissionID",
            id="id",
            response="once",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = response.parse()
        assert_matches_type(PermissionRespondResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_respond(self, client: Opencode) -> None:
        with client.session.permissions.with_streaming_response.respond(
            permission_id="permissionID",
            id="id",
            response="once",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = response.parse()
            assert_matches_type(PermissionRespondResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_respond(self, client: Opencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.session.permissions.with_raw_response.respond(
                permission_id="permissionID",
                id="",
                response="once",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `permission_id` but received ''"):
            client.session.permissions.with_raw_response.respond(
                permission_id="",
                id="id",
                response="once",
            )


class TestAsyncPermissions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_respond(self, async_client: AsyncOpencode) -> None:
        permission = await async_client.session.permissions.respond(
            permission_id="permissionID",
            id="id",
            response="once",
        )
        assert_matches_type(PermissionRespondResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_respond_with_all_params(self, async_client: AsyncOpencode) -> None:
        permission = await async_client.session.permissions.respond(
            permission_id="permissionID",
            id="id",
            response="once",
            directory="directory",
        )
        assert_matches_type(PermissionRespondResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_respond(self, async_client: AsyncOpencode) -> None:
        response = await async_client.session.permissions.with_raw_response.respond(
            permission_id="permissionID",
            id="id",
            response="once",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        permission = await response.parse()
        assert_matches_type(PermissionRespondResponse, permission, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_respond(self, async_client: AsyncOpencode) -> None:
        async with async_client.session.permissions.with_streaming_response.respond(
            permission_id="permissionID",
            id="id",
            response="once",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            permission = await response.parse()
            assert_matches_type(PermissionRespondResponse, permission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_respond(self, async_client: AsyncOpencode) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.session.permissions.with_raw_response.respond(
                permission_id="permissionID",
                id="",
                response="once",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `permission_id` but received ''"):
            await async_client.session.permissions.with_raw_response.respond(
                permission_id="",
                id="id",
                response="once",
            )
