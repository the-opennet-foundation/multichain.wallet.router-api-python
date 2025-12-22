# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestChains:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: MultichainWalletRouterAPI) -> None:
        chain = client.evm.chains.retrieve(
            "ethereum",
        )
        assert chain is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.chains.with_raw_response.retrieve(
            "ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chain = response.parse()
        assert chain is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.chains.with_streaming_response.retrieve(
            "ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chain = response.parse()
            assert chain is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: MultichainWalletRouterAPI) -> None:
        chain = client.evm.chains.list()
        assert chain is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.chains.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chain = response.parse()
        assert chain is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.chains.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chain = response.parse()
            assert chain is None

        assert cast(Any, response.is_closed) is True


class TestAsyncChains:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        chain = await async_client.evm.chains.retrieve(
            "ethereum",
        )
        assert chain is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.chains.with_raw_response.retrieve(
            "ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chain = await response.parse()
        assert chain is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.chains.with_streaming_response.retrieve(
            "ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chain = await response.parse()
            assert chain is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        chain = await async_client.evm.chains.list()
        assert chain is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.chains.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        chain = await response.parse()
        assert chain is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.chains.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            chain = await response.parse()
            assert chain is None

        assert cast(Any, response.is_closed) is True
