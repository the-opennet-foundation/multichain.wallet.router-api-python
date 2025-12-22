# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWallet:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_chains(self, client: MultichainWalletRouterAPI) -> None:
        wallet = client.wallet.list_chains()
        assert wallet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_chains(self, client: MultichainWalletRouterAPI) -> None:
        response = client.wallet.with_raw_response.list_chains()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert wallet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_chains(self, client: MultichainWalletRouterAPI) -> None:
        with client.wallet.with_streaming_response.list_chains() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert wallet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_chain(self, client: MultichainWalletRouterAPI) -> None:
        wallet = client.wallet.retrieve_chain(
            "ethereum",
        )
        assert wallet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_chain(self, client: MultichainWalletRouterAPI) -> None:
        response = client.wallet.with_raw_response.retrieve_chain(
            "ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert wallet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_chain(self, client: MultichainWalletRouterAPI) -> None:
        with client.wallet.with_streaming_response.retrieve_chain(
            "ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert wallet is None

        assert cast(Any, response.is_closed) is True


class TestAsyncWallet:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_chains(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        wallet = await async_client.wallet.list_chains()
        assert wallet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_chains(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.wallet.with_raw_response.list_chains()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert wallet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_chains(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.wallet.with_streaming_response.list_chains() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert wallet is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_chain(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        wallet = await async_client.wallet.retrieve_chain(
            "ethereum",
        )
        assert wallet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_chain(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.wallet.with_raw_response.retrieve_chain(
            "ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert wallet is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_chain(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.wallet.with_streaming_response.retrieve_chain(
            "ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert wallet is None

        assert cast(Any, response.is_closed) is True
