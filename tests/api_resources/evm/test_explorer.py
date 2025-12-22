# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExplorer:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_gas_oracle(self, client: MultichainWalletRouterAPI) -> None:
        explorer = client.evm.explorer.get_gas_oracle(
            "ethereum",
        )
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_gas_oracle(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.explorer.with_raw_response.get_gas_oracle(
            "ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        explorer = response.parse()
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_gas_oracle(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.explorer.with_streaming_response.get_gas_oracle(
            "ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            explorer = response.parse()
            assert explorer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_token_info(self, client: MultichainWalletRouterAPI) -> None:
        explorer = client.evm.explorer.get_token_info(
            address="address",
            chain_id="ethereum",
        )
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_token_info(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.explorer.with_raw_response.get_token_info(
            address="address",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        explorer = response.parse()
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_token_info(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.explorer.with_streaming_response.get_token_info(
            address="address",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            explorer = response.parse()
            assert explorer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_token_info(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.evm.explorer.with_raw_response.get_token_info(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_tokentx(self, client: MultichainWalletRouterAPI) -> None:
        explorer = client.evm.explorer.get_tokentx(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_tokentx_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        explorer = client.evm.explorer.get_tokentx(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
            contract_address="contractAddress",
            offset=0,
            page=0,
        )
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_tokentx(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.explorer.with_raw_response.get_tokentx(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        explorer = response.parse()
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_tokentx(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.explorer.with_streaming_response.get_tokentx(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            explorer = response.parse()
            assert explorer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_tokentx(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.evm.explorer.with_raw_response.get_tokentx(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_txlist(self, client: MultichainWalletRouterAPI) -> None:
        explorer = client.evm.explorer.get_txlist(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_txlist_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        explorer = client.evm.explorer.get_txlist(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
            offset=0,
            page=0,
            sort="asc",
        )
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_txlist(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.explorer.with_raw_response.get_txlist(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        explorer = response.parse()
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_txlist(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.explorer.with_streaming_response.get_txlist(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            explorer = response.parse()
            assert explorer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_txlist(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.evm.explorer.with_raw_response.get_txlist(
                address="",
                chain_id="ethereum",
            )


class TestAsyncExplorer:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_gas_oracle(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        explorer = await async_client.evm.explorer.get_gas_oracle(
            "ethereum",
        )
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_gas_oracle(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.explorer.with_raw_response.get_gas_oracle(
            "ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        explorer = await response.parse()
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_gas_oracle(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.explorer.with_streaming_response.get_gas_oracle(
            "ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            explorer = await response.parse()
            assert explorer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_token_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        explorer = await async_client.evm.explorer.get_token_info(
            address="address",
            chain_id="ethereum",
        )
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_token_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.explorer.with_raw_response.get_token_info(
            address="address",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        explorer = await response.parse()
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_token_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.explorer.with_streaming_response.get_token_info(
            address="address",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            explorer = await response.parse()
            assert explorer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_token_info(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.evm.explorer.with_raw_response.get_token_info(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_tokentx(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        explorer = await async_client.evm.explorer.get_tokentx(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_tokentx_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        explorer = await async_client.evm.explorer.get_tokentx(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
            contract_address="contractAddress",
            offset=0,
            page=0,
        )
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_tokentx(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.explorer.with_raw_response.get_tokentx(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        explorer = await response.parse()
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_tokentx(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.explorer.with_streaming_response.get_tokentx(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            explorer = await response.parse()
            assert explorer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_tokentx(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.evm.explorer.with_raw_response.get_tokentx(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_txlist(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        explorer = await async_client.evm.explorer.get_txlist(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_txlist_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        explorer = await async_client.evm.explorer.get_txlist(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
            offset=0,
            page=0,
            sort="asc",
        )
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_txlist(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.explorer.with_raw_response.get_txlist(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        explorer = await response.parse()
        assert explorer is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_txlist(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.explorer.with_streaming_response.get_txlist(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            explorer = await response.parse()
            assert explorer is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_txlist(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.evm.explorer.with_raw_response.get_txlist(
                address="",
                chain_id="ethereum",
            )
