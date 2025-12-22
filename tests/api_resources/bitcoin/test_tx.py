# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTx:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_broadcast(self, client: MultichainWalletRouterAPI) -> None:
        tx = client.bitcoin.tx.broadcast(
            hex="hex",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_broadcast(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.tx.with_raw_response.broadcast(
            hex="hex",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_broadcast(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.tx.with_streaming_response.broadcast(
            hex="hex",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_decode(self, client: MultichainWalletRouterAPI) -> None:
        tx = client.bitcoin.tx.decode(
            hex="hex",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_decode(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.tx.with_raw_response.decode(
            hex="hex",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_decode(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.tx.with_streaming_response.decode(
            hex="hex",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_info(self, client: MultichainWalletRouterAPI) -> None:
        tx = client.bitcoin.tx.get_info(
            "txid",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_info(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.tx.with_raw_response.get_info(
            "txid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_info(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.tx.with_streaming_response.get_info(
            "txid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_info(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `txid` but received ''"):
            client.bitcoin.tx.with_raw_response.get_info(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_raw(self, client: MultichainWalletRouterAPI) -> None:
        tx = client.bitcoin.tx.get_raw(
            txid="txid",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_raw_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        tx = client.bitcoin.tx.get_raw(
            txid="txid",
            verbose=True,
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_raw(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.tx.with_raw_response.get_raw(
            txid="txid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_raw(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.tx.with_streaming_response.get_raw(
            txid="txid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_raw(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `txid` but received ''"):
            client.bitcoin.tx.with_raw_response.get_raw(
                txid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_raw_hex(self, client: MultichainWalletRouterAPI) -> None:
        tx = client.bitcoin.tx.get_raw_hex(
            "txid",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_raw_hex(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.tx.with_raw_response.get_raw_hex(
            "txid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_raw_hex(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.tx.with_streaming_response.get_raw_hex(
            "txid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_raw_hex(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `txid` but received ''"):
            client.bitcoin.tx.with_raw_response.get_raw_hex(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_status(self, client: MultichainWalletRouterAPI) -> None:
        tx = client.bitcoin.tx.get_status(
            "txid",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.tx.with_raw_response.get_status(
            "txid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.tx.with_streaming_response.get_status(
            "txid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `txid` but received ''"):
            client.bitcoin.tx.with_raw_response.get_status(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_test_mempool(self, client: MultichainWalletRouterAPI) -> None:
        tx = client.bitcoin.tx.test_mempool(
            raw_txs=["string"],
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_test_mempool(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.tx.with_raw_response.test_mempool(
            raw_txs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_test_mempool(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.tx.with_streaming_response.test_mempool(
            raw_txs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTx:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_broadcast(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        tx = await async_client.bitcoin.tx.broadcast(
            hex="hex",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_broadcast(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.tx.with_raw_response.broadcast(
            hex="hex",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = await response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_broadcast(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.tx.with_streaming_response.broadcast(
            hex="hex",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = await response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_decode(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        tx = await async_client.bitcoin.tx.decode(
            hex="hex",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_decode(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.tx.with_raw_response.decode(
            hex="hex",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = await response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_decode(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.tx.with_streaming_response.decode(
            hex="hex",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = await response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        tx = await async_client.bitcoin.tx.get_info(
            "txid",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.tx.with_raw_response.get_info(
            "txid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = await response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.tx.with_streaming_response.get_info(
            "txid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = await response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `txid` but received ''"):
            await async_client.bitcoin.tx.with_raw_response.get_info(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_raw(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        tx = await async_client.bitcoin.tx.get_raw(
            txid="txid",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_raw_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        tx = await async_client.bitcoin.tx.get_raw(
            txid="txid",
            verbose=True,
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_raw(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.tx.with_raw_response.get_raw(
            txid="txid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = await response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_raw(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.tx.with_streaming_response.get_raw(
            txid="txid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = await response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_raw(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `txid` but received ''"):
            await async_client.bitcoin.tx.with_raw_response.get_raw(
                txid="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_raw_hex(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        tx = await async_client.bitcoin.tx.get_raw_hex(
            "txid",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_raw_hex(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.tx.with_raw_response.get_raw_hex(
            "txid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = await response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_raw_hex(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.tx.with_streaming_response.get_raw_hex(
            "txid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = await response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_raw_hex(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `txid` but received ''"):
            await async_client.bitcoin.tx.with_raw_response.get_raw_hex(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        tx = await async_client.bitcoin.tx.get_status(
            "txid",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.tx.with_raw_response.get_status(
            "txid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = await response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.tx.with_streaming_response.get_status(
            "txid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = await response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `txid` but received ''"):
            await async_client.bitcoin.tx.with_raw_response.get_status(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_test_mempool(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        tx = await async_client.bitcoin.tx.test_mempool(
            raw_txs=["string"],
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_test_mempool(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.tx.with_raw_response.test_mempool(
            raw_txs=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = await response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_test_mempool(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.tx.with_streaming_response.test_mempool(
            raw_txs=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = await response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True
