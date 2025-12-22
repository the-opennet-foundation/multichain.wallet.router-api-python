# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSolana:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_multiple_accounts(self, client: MultichainWalletRouterAPI) -> None:
        solana = client.solana.create_multiple_accounts()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_multiple_accounts_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        solana = client.solana.create_multiple_accounts(
            addresses=["string"],
        )
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_multiple_accounts(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.with_raw_response.create_multiple_accounts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_multiple_accounts(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.with_streaming_response.create_multiple_accounts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_signatures(self, client: MultichainWalletRouterAPI) -> None:
        solana = client.solana.list_signatures(
            address="address",
        )
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_signatures_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        solana = client.solana.list_signatures(
            address="address",
            before="before",
            limit=1000,
            until="until",
        )
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_signatures(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.with_raw_response.list_signatures(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_signatures(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.with_streaming_response.list_signatures(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_signatures(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.solana.with_raw_response.list_signatures(
                address="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_tokens(self, client: MultichainWalletRouterAPI) -> None:
        solana = client.solana.list_tokens(
            owner="owner",
        )
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_tokens_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        solana = client.solana.list_tokens(
            owner="owner",
            mint="mint",
            program_id="programId",
        )
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_tokens(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.with_raw_response.list_tokens(
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_tokens(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.with_streaming_response.list_tokens(
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_tokens(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            client.solana.with_raw_response.list_tokens(
                owner="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_validators(self, client: MultichainWalletRouterAPI) -> None:
        solana = client.solana.list_validators()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_validators(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.with_raw_response.list_validators()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_validators(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.with_streaming_response.list_validators() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_account_info(self, client: MultichainWalletRouterAPI) -> None:
        solana = client.solana.retrieve_account_info(
            "address",
        )
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_account_info(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.with_raw_response.retrieve_account_info(
            "address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_account_info(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.with_streaming_response.retrieve_account_info(
            "address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_account_info(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.solana.with_raw_response.retrieve_account_info(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_balance(self, client: MultichainWalletRouterAPI) -> None:
        solana = client.solana.retrieve_balance(
            "address",
        )
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_balance(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.with_raw_response.retrieve_balance(
            "address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_balance(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.with_streaming_response.retrieve_balance(
            "address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_balance(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.solana.with_raw_response.retrieve_balance(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_block_by_slot(self, client: MultichainWalletRouterAPI) -> None:
        solana = client.solana.retrieve_block_by_slot(
            0,
        )
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_block_by_slot(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.with_raw_response.retrieve_block_by_slot(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_block_by_slot(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.with_streaming_response.retrieve_block_by_slot(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_current_slot(self, client: MultichainWalletRouterAPI) -> None:
        solana = client.solana.retrieve_current_slot()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_current_slot(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.with_raw_response.retrieve_current_slot()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_current_slot(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.with_streaming_response.retrieve_current_slot() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_info(self, client: MultichainWalletRouterAPI) -> None:
        solana = client.solana.retrieve_info()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_info(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.with_raw_response.retrieve_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_info(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.with_streaming_response.retrieve_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_latest_blockhash(self, client: MultichainWalletRouterAPI) -> None:
        solana = client.solana.retrieve_latest_blockhash()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_latest_blockhash(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.with_raw_response.retrieve_latest_blockhash()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_latest_blockhash(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.with_streaming_response.retrieve_latest_blockhash() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True


class TestAsyncSolana:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_multiple_accounts(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        solana = await async_client.solana.create_multiple_accounts()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_multiple_accounts_with_all_params(
        self, async_client: AsyncMultichainWalletRouterAPI
    ) -> None:
        solana = await async_client.solana.create_multiple_accounts(
            addresses=["string"],
        )
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_multiple_accounts(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.with_raw_response.create_multiple_accounts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = await response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_multiple_accounts(
        self, async_client: AsyncMultichainWalletRouterAPI
    ) -> None:
        async with async_client.solana.with_streaming_response.create_multiple_accounts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = await response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_signatures(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        solana = await async_client.solana.list_signatures(
            address="address",
        )
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_signatures_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        solana = await async_client.solana.list_signatures(
            address="address",
            before="before",
            limit=1000,
            until="until",
        )
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_signatures(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.with_raw_response.list_signatures(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = await response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_signatures(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.with_streaming_response.list_signatures(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = await response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_signatures(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.solana.with_raw_response.list_signatures(
                address="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_tokens(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        solana = await async_client.solana.list_tokens(
            owner="owner",
        )
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_tokens_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        solana = await async_client.solana.list_tokens(
            owner="owner",
            mint="mint",
            program_id="programId",
        )
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_tokens(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.with_raw_response.list_tokens(
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = await response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_tokens(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.with_streaming_response.list_tokens(
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = await response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_tokens(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            await async_client.solana.with_raw_response.list_tokens(
                owner="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_validators(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        solana = await async_client.solana.list_validators()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_validators(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.with_raw_response.list_validators()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = await response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_validators(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.with_streaming_response.list_validators() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = await response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_account_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        solana = await async_client.solana.retrieve_account_info(
            "address",
        )
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_account_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.with_raw_response.retrieve_account_info(
            "address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = await response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_account_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.with_streaming_response.retrieve_account_info(
            "address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = await response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_account_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.solana.with_raw_response.retrieve_account_info(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_balance(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        solana = await async_client.solana.retrieve_balance(
            "address",
        )
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_balance(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.with_raw_response.retrieve_balance(
            "address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = await response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_balance(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.with_streaming_response.retrieve_balance(
            "address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = await response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_balance(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.solana.with_raw_response.retrieve_balance(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_block_by_slot(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        solana = await async_client.solana.retrieve_block_by_slot(
            0,
        )
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_block_by_slot(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.with_raw_response.retrieve_block_by_slot(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = await response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_block_by_slot(
        self, async_client: AsyncMultichainWalletRouterAPI
    ) -> None:
        async with async_client.solana.with_streaming_response.retrieve_block_by_slot(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = await response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_current_slot(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        solana = await async_client.solana.retrieve_current_slot()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_current_slot(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.with_raw_response.retrieve_current_slot()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = await response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_current_slot(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.with_streaming_response.retrieve_current_slot() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = await response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        solana = await async_client.solana.retrieve_info()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.with_raw_response.retrieve_info()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = await response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.with_streaming_response.retrieve_info() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = await response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_latest_blockhash(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        solana = await async_client.solana.retrieve_latest_blockhash()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_latest_blockhash(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.with_raw_response.retrieve_latest_blockhash()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        solana = await response.parse()
        assert solana is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_latest_blockhash(
        self, async_client: AsyncMultichainWalletRouterAPI
    ) -> None:
        async with async_client.solana.with_streaming_response.retrieve_latest_blockhash() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            solana = await response.parse()
            assert solana is None

        assert cast(Any, response.is_closed) is True
