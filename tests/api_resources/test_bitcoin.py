# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBitcoin:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_difficulty(self, client: MultichainWalletRouterAPI) -> None:
        bitcoin = client.bitcoin.get_difficulty()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_difficulty(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.with_raw_response.get_difficulty()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bitcoin = response.parse()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_difficulty(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.with_streaming_response.get_difficulty() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bitcoin = response.parse()
            assert bitcoin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_hashrate(self, client: MultichainWalletRouterAPI) -> None:
        bitcoin = client.bitcoin.get_hashrate()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_hashrate_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        bitcoin = client.bitcoin.get_hashrate(
            height=0,
            nblocks=0,
        )
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_hashrate(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.with_raw_response.get_hashrate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bitcoin = response.parse()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_hashrate(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.with_streaming_response.get_hashrate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bitcoin = response.parse()
            assert bitcoin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_info(self, client: MultichainWalletRouterAPI) -> None:
        bitcoin = client.bitcoin.get_info()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_info(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.with_raw_response.get_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bitcoin = response.parse()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_info(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.with_streaming_response.get_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bitcoin = response.parse()
            assert bitcoin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_price(self, client: MultichainWalletRouterAPI) -> None:
        bitcoin = client.bitcoin.get_price()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_price(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.with_raw_response.get_price()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bitcoin = response.parse()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_price(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.with_streaming_response.get_price() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bitcoin = response.parse()
            assert bitcoin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_utxo(self, client: MultichainWalletRouterAPI) -> None:
        bitcoin = client.bitcoin.get_utxo(
            vout=0,
            txid="txid",
        )
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_utxo_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        bitcoin = client.bitcoin.get_utxo(
            vout=0,
            txid="txid",
            include_mempool=True,
        )
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_utxo(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.with_raw_response.get_utxo(
            vout=0,
            txid="txid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bitcoin = response.parse()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_utxo(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.with_streaming_response.get_utxo(
            vout=0,
            txid="txid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bitcoin = response.parse()
            assert bitcoin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_utxo(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `txid` but received ''"):
            client.bitcoin.with_raw_response.get_utxo(
                vout=0,
                txid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_validate_address(self, client: MultichainWalletRouterAPI) -> None:
        bitcoin = client.bitcoin.validate_address(
            "address",
        )
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_validate_address(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.with_raw_response.validate_address(
            "address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bitcoin = response.parse()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_validate_address(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.with_streaming_response.validate_address(
            "address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bitcoin = response.parse()
            assert bitcoin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_validate_address(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.bitcoin.with_raw_response.validate_address(
                "",
            )


class TestAsyncBitcoin:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_difficulty(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        bitcoin = await async_client.bitcoin.get_difficulty()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_difficulty(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.with_raw_response.get_difficulty()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bitcoin = await response.parse()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_difficulty(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.with_streaming_response.get_difficulty() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bitcoin = await response.parse()
            assert bitcoin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_hashrate(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        bitcoin = await async_client.bitcoin.get_hashrate()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_hashrate_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        bitcoin = await async_client.bitcoin.get_hashrate(
            height=0,
            nblocks=0,
        )
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_hashrate(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.with_raw_response.get_hashrate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bitcoin = await response.parse()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_hashrate(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.with_streaming_response.get_hashrate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bitcoin = await response.parse()
            assert bitcoin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        bitcoin = await async_client.bitcoin.get_info()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.with_raw_response.get_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bitcoin = await response.parse()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.with_streaming_response.get_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bitcoin = await response.parse()
            assert bitcoin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_price(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        bitcoin = await async_client.bitcoin.get_price()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_price(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.with_raw_response.get_price()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bitcoin = await response.parse()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_price(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.with_streaming_response.get_price() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bitcoin = await response.parse()
            assert bitcoin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_utxo(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        bitcoin = await async_client.bitcoin.get_utxo(
            vout=0,
            txid="txid",
        )
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_utxo_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        bitcoin = await async_client.bitcoin.get_utxo(
            vout=0,
            txid="txid",
            include_mempool=True,
        )
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_utxo(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.with_raw_response.get_utxo(
            vout=0,
            txid="txid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bitcoin = await response.parse()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_utxo(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.with_streaming_response.get_utxo(
            vout=0,
            txid="txid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bitcoin = await response.parse()
            assert bitcoin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_utxo(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `txid` but received ''"):
            await async_client.bitcoin.with_raw_response.get_utxo(
                vout=0,
                txid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_validate_address(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        bitcoin = await async_client.bitcoin.validate_address(
            "address",
        )
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_validate_address(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.with_raw_response.validate_address(
            "address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bitcoin = await response.parse()
        assert bitcoin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_validate_address(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.with_streaming_response.validate_address(
            "address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bitcoin = await response.parse()
            assert bitcoin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_validate_address(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.bitcoin.with_raw_response.validate_address(
                "",
            )
