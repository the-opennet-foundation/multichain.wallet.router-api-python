# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestToken:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_largest_accounts(self, client: MultichainWalletRouterAPI) -> None:
        token = client.solana.token.list_largest_accounts(
            "mint",
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_largest_accounts(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.token.with_raw_response.list_largest_accounts(
            "mint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_largest_accounts(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.token.with_streaming_response.list_largest_accounts(
            "mint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_largest_accounts(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mint` but received ''"):
            client.solana.token.with_raw_response.list_largest_accounts(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_balance(self, client: MultichainWalletRouterAPI) -> None:
        token = client.solana.token.retrieve_balance(
            "tokenAccount",
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_balance(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.token.with_raw_response.retrieve_balance(
            "tokenAccount",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_balance(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.token.with_streaming_response.retrieve_balance(
            "tokenAccount",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_balance(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_account` but received ''"):
            client.solana.token.with_raw_response.retrieve_balance(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_total_supply(self, client: MultichainWalletRouterAPI) -> None:
        token = client.solana.token.retrieve_total_supply(
            "mint",
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_total_supply(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.token.with_raw_response.retrieve_total_supply(
            "mint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_total_supply(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.token.with_streaming_response.retrieve_total_supply(
            "mint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_total_supply(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mint` but received ''"):
            client.solana.token.with_raw_response.retrieve_total_supply(
                "",
            )


class TestAsyncToken:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_largest_accounts(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        token = await async_client.solana.token.list_largest_accounts(
            "mint",
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_largest_accounts(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.token.with_raw_response.list_largest_accounts(
            "mint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_largest_accounts(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.token.with_streaming_response.list_largest_accounts(
            "mint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_largest_accounts(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mint` but received ''"):
            await async_client.solana.token.with_raw_response.list_largest_accounts(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_balance(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        token = await async_client.solana.token.retrieve_balance(
            "tokenAccount",
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_balance(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.token.with_raw_response.retrieve_balance(
            "tokenAccount",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_balance(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.token.with_streaming_response.retrieve_balance(
            "tokenAccount",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_balance(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_account` but received ''"):
            await async_client.solana.token.with_raw_response.retrieve_balance(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_total_supply(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        token = await async_client.solana.token.retrieve_total_supply(
            "mint",
        )
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_total_supply(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.token.with_raw_response.retrieve_total_supply(
            "mint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert token is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_total_supply(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.token.with_streaming_response.retrieve_total_supply(
            "mint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert token is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_total_supply(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `mint` but received ''"):
            await async_client.solana.token.with_raw_response.retrieve_total_supply(
                "",
            )
