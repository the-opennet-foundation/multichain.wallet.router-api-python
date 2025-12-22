# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMempool:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_info(self, client: MultichainWalletRouterAPI) -> None:
        mempool = client.bitcoin.mempool.get_info()
        assert mempool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_info(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.mempool.with_raw_response.get_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mempool = response.parse()
        assert mempool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_info(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.mempool.with_streaming_response.get_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mempool = response.parse()
            assert mempool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_projected_blocks(self, client: MultichainWalletRouterAPI) -> None:
        mempool = client.bitcoin.mempool.get_projected_blocks()
        assert mempool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_projected_blocks(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.mempool.with_raw_response.get_projected_blocks()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mempool = response.parse()
        assert mempool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_projected_blocks(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.mempool.with_streaming_response.get_projected_blocks() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mempool = response.parse()
            assert mempool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_raw(self, client: MultichainWalletRouterAPI) -> None:
        mempool = client.bitcoin.mempool.get_raw()
        assert mempool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_raw_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        mempool = client.bitcoin.mempool.get_raw(
            verbose=True,
        )
        assert mempool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_raw(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.mempool.with_raw_response.get_raw()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mempool = response.parse()
        assert mempool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_raw(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.mempool.with_streaming_response.get_raw() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mempool = response.parse()
            assert mempool is None

        assert cast(Any, response.is_closed) is True


class TestAsyncMempool:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        mempool = await async_client.bitcoin.mempool.get_info()
        assert mempool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.mempool.with_raw_response.get_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mempool = await response.parse()
        assert mempool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.mempool.with_streaming_response.get_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mempool = await response.parse()
            assert mempool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_projected_blocks(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        mempool = await async_client.bitcoin.mempool.get_projected_blocks()
        assert mempool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_projected_blocks(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.mempool.with_raw_response.get_projected_blocks()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mempool = await response.parse()
        assert mempool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_projected_blocks(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.mempool.with_streaming_response.get_projected_blocks() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mempool = await response.parse()
            assert mempool is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_raw(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        mempool = await async_client.bitcoin.mempool.get_raw()
        assert mempool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_raw_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        mempool = await async_client.bitcoin.mempool.get_raw(
            verbose=True,
        )
        assert mempool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_raw(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.mempool.with_raw_response.get_raw()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        mempool = await response.parse()
        assert mempool is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_raw(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.mempool.with_streaming_response.get_raw() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            mempool = await response.parse()
            assert mempool is None

        assert cast(Any, response.is_closed) is True
