# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInflation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_rate(self, client: MultichainWalletRouterAPI) -> None:
        inflation = client.solana.inflation.get_rate()
        assert inflation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_rate(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.inflation.with_raw_response.get_rate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inflation = response.parse()
        assert inflation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_rate(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.inflation.with_streaming_response.get_rate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inflation = response.parse()
            assert inflation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_rewards(self, client: MultichainWalletRouterAPI) -> None:
        inflation = client.solana.inflation.get_rewards(
            addresses=["string"],
        )
        assert inflation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_rewards_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        inflation = client.solana.inflation.get_rewards(
            addresses=["string"],
            epoch=0,
        )
        assert inflation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_rewards(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.inflation.with_raw_response.get_rewards(
            addresses=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inflation = response.parse()
        assert inflation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_rewards(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.inflation.with_streaming_response.get_rewards(
            addresses=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inflation = response.parse()
            assert inflation is None

        assert cast(Any, response.is_closed) is True


class TestAsyncInflation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_rate(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        inflation = await async_client.solana.inflation.get_rate()
        assert inflation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_rate(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.inflation.with_raw_response.get_rate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inflation = await response.parse()
        assert inflation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_rate(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.inflation.with_streaming_response.get_rate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inflation = await response.parse()
            assert inflation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_rewards(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        inflation = await async_client.solana.inflation.get_rewards(
            addresses=["string"],
        )
        assert inflation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_rewards_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        inflation = await async_client.solana.inflation.get_rewards(
            addresses=["string"],
            epoch=0,
        )
        assert inflation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_rewards(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.inflation.with_raw_response.get_rewards(
            addresses=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inflation = await response.parse()
        assert inflation is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_rewards(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.inflation.with_streaming_response.get_rewards(
            addresses=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inflation = await response.parse()
            assert inflation is None

        assert cast(Any, response.is_closed) is True
