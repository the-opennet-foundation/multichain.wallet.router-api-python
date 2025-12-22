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
    def test_method_retrieve(self, client: MultichainWalletRouterAPI) -> None:
        tx = client.solana.tx.retrieve(
            "signature",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.tx.with_raw_response.retrieve(
            "signature",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.tx.with_streaming_response.retrieve(
            "signature",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `signature` but received ''"):
            client.solana.tx.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send(self, client: MultichainWalletRouterAPI) -> None:
        tx = client.solana.tx.send(
            signed_transaction="signedTransaction",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.tx.with_raw_response.send(
            signed_transaction="signedTransaction",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.tx.with_streaming_response.send(
            signed_transaction="signedTransaction",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_simulate(self, client: MultichainWalletRouterAPI) -> None:
        tx = client.solana.tx.simulate(
            transaction="transaction",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_simulate(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.tx.with_raw_response.simulate(
            transaction="transaction",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_simulate(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.tx.with_streaming_response.simulate(
            transaction="transaction",
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
    async def test_method_retrieve(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        tx = await async_client.solana.tx.retrieve(
            "signature",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.tx.with_raw_response.retrieve(
            "signature",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = await response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.tx.with_streaming_response.retrieve(
            "signature",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = await response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `signature` but received ''"):
            await async_client.solana.tx.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        tx = await async_client.solana.tx.send(
            signed_transaction="signedTransaction",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.tx.with_raw_response.send(
            signed_transaction="signedTransaction",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = await response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.tx.with_streaming_response.send(
            signed_transaction="signedTransaction",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = await response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_simulate(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        tx = await async_client.solana.tx.simulate(
            transaction="transaction",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_simulate(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.tx.with_raw_response.simulate(
            transaction="transaction",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = await response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_simulate(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.tx.with_streaming_response.simulate(
            transaction="transaction",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = await response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True
