# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFees:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_priority(self, client: MultichainWalletRouterAPI) -> None:
        fee = client.solana.fees.get_priority()
        assert fee is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_priority_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        fee = client.solana.fees.get_priority(
            account_keys="accountKeys",
        )
        assert fee is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_priority(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.fees.with_raw_response.get_priority()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fee = response.parse()
        assert fee is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_priority(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.fees.with_streaming_response.get_priority() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fee = response.parse()
            assert fee is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_recent(self, client: MultichainWalletRouterAPI) -> None:
        fee = client.solana.fees.get_recent()
        assert fee is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_recent_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        fee = client.solana.fees.get_recent(
            addresses="addresses",
        )
        assert fee is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_recent(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.fees.with_raw_response.get_recent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fee = response.parse()
        assert fee is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_recent(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.fees.with_streaming_response.get_recent() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fee = response.parse()
            assert fee is None

        assert cast(Any, response.is_closed) is True


class TestAsyncFees:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_priority(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        fee = await async_client.solana.fees.get_priority()
        assert fee is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_priority_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        fee = await async_client.solana.fees.get_priority(
            account_keys="accountKeys",
        )
        assert fee is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_priority(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.fees.with_raw_response.get_priority()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fee = await response.parse()
        assert fee is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_priority(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.fees.with_streaming_response.get_priority() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fee = await response.parse()
            assert fee is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_recent(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        fee = await async_client.solana.fees.get_recent()
        assert fee is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_recent_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        fee = await async_client.solana.fees.get_recent(
            addresses="addresses",
        )
        assert fee is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_recent(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.fees.with_raw_response.get_recent()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fee = await response.parse()
        assert fee is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_recent(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.fees.with_streaming_response.get_recent() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fee = await response.parse()
            assert fee is None

        assert cast(Any, response.is_closed) is True
