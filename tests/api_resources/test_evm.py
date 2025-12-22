# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvm:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_call_contract(self, client: MultichainWalletRouterAPI) -> None:
        evm = client.evm.call_contract(
            chain_id="ethereum",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_call_contract_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        evm = client.evm.call_contract(
            chain_id="ethereum",
            block_tag="blockTag",
            transaction={
                "data": "data",
                "to": "to",
            },
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_call_contract(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.with_raw_response.call_contract(
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_call_contract(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.with_streaming_response.call_contract(
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_balance(self, client: MultichainWalletRouterAPI) -> None:
        evm = client.evm.get_balance(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_balance(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.with_raw_response.get_balance(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_balance(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.with_streaming_response.get_balance(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_balance(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.evm.with_raw_response.get_balance(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_contract_code(self, client: MultichainWalletRouterAPI) -> None:
        evm = client.evm.get_contract_code(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_contract_code(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.with_raw_response.get_contract_code(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_contract_code(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.with_streaming_response.get_contract_code(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_contract_code(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.evm.with_raw_response.get_contract_code(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_nft_metadata(self, client: MultichainWalletRouterAPI) -> None:
        evm = client.evm.get_nft_metadata(
            token_id="tokenId",
            chain_id="ethereum",
            contract_address="contractAddress",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_nft_metadata(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.with_raw_response.get_nft_metadata(
            token_id="tokenId",
            chain_id="ethereum",
            contract_address="contractAddress",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_nft_metadata(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.with_streaming_response.get_nft_metadata(
            token_id="tokenId",
            chain_id="ethereum",
            contract_address="contractAddress",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_nft_metadata(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_address` but received ''"):
            client.evm.with_raw_response.get_nft_metadata(
                token_id="tokenId",
                chain_id="ethereum",
                contract_address="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            client.evm.with_raw_response.get_nft_metadata(
                token_id="",
                chain_id="ethereum",
                contract_address="contractAddress",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_nfts(self, client: MultichainWalletRouterAPI) -> None:
        evm = client.evm.get_nfts(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_nfts_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        evm = client.evm.get_nfts(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
            page_key="pageKey",
            page_size=0,
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_nfts(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.with_raw_response.get_nfts(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_nfts(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.with_streaming_response.get_nfts(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_nfts(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.evm.with_raw_response.get_nfts(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_nonce(self, client: MultichainWalletRouterAPI) -> None:
        evm = client.evm.get_nonce(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_nonce(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.with_raw_response.get_nonce(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_nonce(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.with_streaming_response.get_nonce(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_nonce(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.evm.with_raw_response.get_nonce(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_tokens(self, client: MultichainWalletRouterAPI) -> None:
        evm = client.evm.get_tokens(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_tokens(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.with_raw_response.get_tokens(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_tokens(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.with_streaming_response.get_tokens(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_tokens(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.evm.with_raw_response.get_tokens(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_transaction_history(self, client: MultichainWalletRouterAPI) -> None:
        evm = client.evm.get_transaction_history(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_transaction_history_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        evm = client.evm.get_transaction_history(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
            category="category",
            from_block="fromBlock",
            max_count=0,
            page_key="pageKey",
            to_block="toBlock",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_transaction_history(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.with_raw_response.get_transaction_history(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_transaction_history(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.with_streaming_response.get_transaction_history(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_transaction_history(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.evm.with_raw_response.get_transaction_history(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_simulate_transaction(self, client: MultichainWalletRouterAPI) -> None:
        evm = client.evm.simulate_transaction(
            chain_id="ethereum",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_simulate_transaction_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        evm = client.evm.simulate_transaction(
            chain_id="ethereum",
            transaction={},
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_simulate_transaction(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.with_raw_response.simulate_transaction(
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_simulate_transaction(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.with_streaming_response.simulate_transaction(
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True


class TestAsyncEvm:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_call_contract(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        evm = await async_client.evm.call_contract(
            chain_id="ethereum",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_call_contract_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        evm = await async_client.evm.call_contract(
            chain_id="ethereum",
            block_tag="blockTag",
            transaction={
                "data": "data",
                "to": "to",
            },
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_call_contract(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.with_raw_response.call_contract(
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = await response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_call_contract(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.with_streaming_response.call_contract(
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = await response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_balance(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        evm = await async_client.evm.get_balance(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_balance(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.with_raw_response.get_balance(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = await response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_balance(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.with_streaming_response.get_balance(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = await response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_balance(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.evm.with_raw_response.get_balance(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_contract_code(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        evm = await async_client.evm.get_contract_code(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_contract_code(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.with_raw_response.get_contract_code(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = await response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_contract_code(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.with_streaming_response.get_contract_code(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = await response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_contract_code(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.evm.with_raw_response.get_contract_code(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_nft_metadata(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        evm = await async_client.evm.get_nft_metadata(
            token_id="tokenId",
            chain_id="ethereum",
            contract_address="contractAddress",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_nft_metadata(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.with_raw_response.get_nft_metadata(
            token_id="tokenId",
            chain_id="ethereum",
            contract_address="contractAddress",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = await response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_nft_metadata(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.with_streaming_response.get_nft_metadata(
            token_id="tokenId",
            chain_id="ethereum",
            contract_address="contractAddress",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = await response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_nft_metadata(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `contract_address` but received ''"):
            await async_client.evm.with_raw_response.get_nft_metadata(
                token_id="tokenId",
                chain_id="ethereum",
                contract_address="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `token_id` but received ''"):
            await async_client.evm.with_raw_response.get_nft_metadata(
                token_id="",
                chain_id="ethereum",
                contract_address="contractAddress",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_nfts(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        evm = await async_client.evm.get_nfts(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_nfts_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        evm = await async_client.evm.get_nfts(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
            page_key="pageKey",
            page_size=0,
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_nfts(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.with_raw_response.get_nfts(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = await response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_nfts(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.with_streaming_response.get_nfts(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = await response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_nfts(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.evm.with_raw_response.get_nfts(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_nonce(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        evm = await async_client.evm.get_nonce(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_nonce(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.with_raw_response.get_nonce(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = await response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_nonce(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.with_streaming_response.get_nonce(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = await response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_nonce(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.evm.with_raw_response.get_nonce(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_tokens(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        evm = await async_client.evm.get_tokens(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_tokens(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.with_raw_response.get_tokens(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = await response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_tokens(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.with_streaming_response.get_tokens(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = await response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_tokens(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.evm.with_raw_response.get_tokens(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_transaction_history(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        evm = await async_client.evm.get_transaction_history(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_transaction_history_with_all_params(
        self, async_client: AsyncMultichainWalletRouterAPI
    ) -> None:
        evm = await async_client.evm.get_transaction_history(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
            category="category",
            from_block="fromBlock",
            max_count=0,
            page_key="pageKey",
            to_block="toBlock",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_transaction_history(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.with_raw_response.get_transaction_history(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = await response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_transaction_history(
        self, async_client: AsyncMultichainWalletRouterAPI
    ) -> None:
        async with async_client.evm.with_streaming_response.get_transaction_history(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = await response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_transaction_history(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.evm.with_raw_response.get_transaction_history(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_simulate_transaction(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        evm = await async_client.evm.simulate_transaction(
            chain_id="ethereum",
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_simulate_transaction_with_all_params(
        self, async_client: AsyncMultichainWalletRouterAPI
    ) -> None:
        evm = await async_client.evm.simulate_transaction(
            chain_id="ethereum",
            transaction={},
        )
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_simulate_transaction(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.with_raw_response.simulate_transaction(
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evm = await response.parse()
        assert evm is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_simulate_transaction(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.with_streaming_response.simulate_transaction(
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evm = await response.parse()
            assert evm is None

        assert cast(Any, response.is_closed) is True
