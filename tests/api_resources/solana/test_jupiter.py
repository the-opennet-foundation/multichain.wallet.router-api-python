# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJupiter:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_price(self, client: MultichainWalletRouterAPI) -> None:
        jupiter = client.solana.jupiter.get_price(
            ids="ids",
        )
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_price(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.jupiter.with_raw_response.get_price(
            ids="ids",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        jupiter = response.parse()
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_price(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.jupiter.with_streaming_response.get_price(
            ids="ids",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            jupiter = response.parse()
            assert jupiter is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_quote(self, client: MultichainWalletRouterAPI) -> None:
        jupiter = client.solana.jupiter.get_quote(
            amount=0,
            input_mint="inputMint",
            output_mint="outputMint",
        )
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_quote_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        jupiter = client.solana.jupiter.get_quote(
            amount=0,
            input_mint="inputMint",
            output_mint="outputMint",
            slippage_bps=0,
        )
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_quote(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.jupiter.with_raw_response.get_quote(
            amount=0,
            input_mint="inputMint",
            output_mint="outputMint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        jupiter = response.parse()
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_quote(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.jupiter.with_streaming_response.get_quote(
            amount=0,
            input_mint="inputMint",
            output_mint="outputMint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            jupiter = response.parse()
            assert jupiter is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_tokens(self, client: MultichainWalletRouterAPI) -> None:
        jupiter = client.solana.jupiter.get_tokens()
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_tokens(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.jupiter.with_raw_response.get_tokens()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        jupiter = response.parse()
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_tokens(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.jupiter.with_streaming_response.get_tokens() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            jupiter = response.parse()
            assert jupiter is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_swap(self, client: MultichainWalletRouterAPI) -> None:
        jupiter = client.solana.jupiter.swap(
            quote_response={},
            user_public_key="userPublicKey",
        )
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_swap(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.jupiter.with_raw_response.swap(
            quote_response={},
            user_public_key="userPublicKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        jupiter = response.parse()
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_swap(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.jupiter.with_streaming_response.swap(
            quote_response={},
            user_public_key="userPublicKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            jupiter = response.parse()
            assert jupiter is None

        assert cast(Any, response.is_closed) is True


class TestAsyncJupiter:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_price(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        jupiter = await async_client.solana.jupiter.get_price(
            ids="ids",
        )
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_price(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.jupiter.with_raw_response.get_price(
            ids="ids",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        jupiter = await response.parse()
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_price(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.jupiter.with_streaming_response.get_price(
            ids="ids",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            jupiter = await response.parse()
            assert jupiter is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_quote(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        jupiter = await async_client.solana.jupiter.get_quote(
            amount=0,
            input_mint="inputMint",
            output_mint="outputMint",
        )
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_quote_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        jupiter = await async_client.solana.jupiter.get_quote(
            amount=0,
            input_mint="inputMint",
            output_mint="outputMint",
            slippage_bps=0,
        )
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_quote(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.jupiter.with_raw_response.get_quote(
            amount=0,
            input_mint="inputMint",
            output_mint="outputMint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        jupiter = await response.parse()
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_quote(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.jupiter.with_streaming_response.get_quote(
            amount=0,
            input_mint="inputMint",
            output_mint="outputMint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            jupiter = await response.parse()
            assert jupiter is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_tokens(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        jupiter = await async_client.solana.jupiter.get_tokens()
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_tokens(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.jupiter.with_raw_response.get_tokens()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        jupiter = await response.parse()
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_tokens(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.jupiter.with_streaming_response.get_tokens() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            jupiter = await response.parse()
            assert jupiter is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_swap(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        jupiter = await async_client.solana.jupiter.swap(
            quote_response={},
            user_public_key="userPublicKey",
        )
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_swap(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.jupiter.with_raw_response.swap(
            quote_response={},
            user_public_key="userPublicKey",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        jupiter = await response.parse()
        assert jupiter is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_swap(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.jupiter.with_streaming_response.swap(
            quote_response={},
            user_public_key="userPublicKey",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            jupiter = await response.parse()
            assert jupiter is None

        assert cast(Any, response.is_closed) is True
