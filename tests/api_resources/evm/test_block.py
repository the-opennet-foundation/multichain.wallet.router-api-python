# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBlock:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_number(self, client: MultichainWalletRouterAPI) -> None:
        block = client.evm.block.get_by_number(
            block_number="blockNumber",
            chain_id="ethereum",
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_number_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        block = client.evm.block.get_by_number(
            block_number="blockNumber",
            chain_id="ethereum",
            full_txs=True,
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_by_number(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.block.with_raw_response.get_by_number(
            block_number="blockNumber",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_by_number(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.block.with_streaming_response.get_by_number(
            block_number="blockNumber",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_by_number(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_number` but received ''"):
            client.evm.block.with_raw_response.get_by_number(
                block_number="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_current_number(self, client: MultichainWalletRouterAPI) -> None:
        block = client.evm.block.get_current_number(
            "ethereum",
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_current_number(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.block.with_raw_response.get_current_number(
            "ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_current_number(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.block.with_streaming_response.get_current_number(
            "ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True


class TestAsyncBlock:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_number(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        block = await async_client.evm.block.get_by_number(
            block_number="blockNumber",
            chain_id="ethereum",
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_number_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        block = await async_client.evm.block.get_by_number(
            block_number="blockNumber",
            chain_id="ethereum",
            full_txs=True,
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_by_number(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.block.with_raw_response.get_by_number(
            block_number="blockNumber",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_number(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.block.with_streaming_response.get_by_number(
            block_number="blockNumber",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_by_number(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_number` but received ''"):
            await async_client.evm.block.with_raw_response.get_by_number(
                block_number="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_current_number(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        block = await async_client.evm.block.get_current_number(
            "ethereum",
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_current_number(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.block.with_raw_response.get_current_number(
            "ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_current_number(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.block.with_streaming_response.get_current_number(
            "ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True
