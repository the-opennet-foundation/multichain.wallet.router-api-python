# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNFT:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_editions(self, client: MultichainWalletRouterAPI) -> None:
        nft = client.solana.nft.get_editions(
            mint="mint",
        )
        assert nft is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_editions_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        nft = client.solana.nft.get_editions(
            mint="mint",
            limit=0,
            page=0,
        )
        assert nft is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_editions(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.nft.with_raw_response.get_editions(
            mint="mint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nft = response.parse()
        assert nft is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_editions(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.nft.with_streaming_response.get_editions(
            mint="mint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nft = response.parse()
            assert nft is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_editions(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mint` but received ''"):
            client.solana.nft.with_raw_response.get_editions(
                mint="",
            )


class TestAsyncNFT:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_editions(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        nft = await async_client.solana.nft.get_editions(
            mint="mint",
        )
        assert nft is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_editions_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        nft = await async_client.solana.nft.get_editions(
            mint="mint",
            limit=0,
            page=0,
        )
        assert nft is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_editions(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.nft.with_raw_response.get_editions(
            mint="mint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        nft = await response.parse()
        assert nft is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_editions(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.nft.with_streaming_response.get_editions(
            mint="mint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            nft = await response.parse()
            assert nft is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_editions(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mint` but received ''"):
            await async_client.solana.nft.with_raw_response.get_editions(
                mint="",
            )
