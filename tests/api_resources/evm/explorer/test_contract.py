# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestContract:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_abi(self, client: MultichainWalletRouterAPI) -> None:
        contract = client.evm.explorer.contract.get_abi(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert contract is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_abi(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.explorer.contract.with_raw_response.get_abi(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert contract is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_abi(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.explorer.contract.with_streaming_response.get_abi(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert contract is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_abi(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.evm.explorer.contract.with_raw_response.get_abi(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_source(self, client: MultichainWalletRouterAPI) -> None:
        contract = client.evm.explorer.contract.get_source(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert contract is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_source(self, client: MultichainWalletRouterAPI) -> None:
        response = client.evm.explorer.contract.with_raw_response.get_source(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = response.parse()
        assert contract is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_source(self, client: MultichainWalletRouterAPI) -> None:
        with client.evm.explorer.contract.with_streaming_response.get_source(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = response.parse()
            assert contract is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_source(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.evm.explorer.contract.with_raw_response.get_source(
                address="",
                chain_id="ethereum",
            )


class TestAsyncContract:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_abi(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        contract = await async_client.evm.explorer.contract.get_abi(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert contract is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_abi(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.explorer.contract.with_raw_response.get_abi(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert contract is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_abi(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.explorer.contract.with_streaming_response.get_abi(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert contract is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_abi(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.evm.explorer.contract.with_raw_response.get_abi(
                address="",
                chain_id="ethereum",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_source(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        contract = await async_client.evm.explorer.contract.get_source(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )
        assert contract is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_source(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.evm.explorer.contract.with_raw_response.get_source(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        contract = await response.parse()
        assert contract is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_source(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.evm.explorer.contract.with_streaming_response.get_source(
            address="0x2c02efDd09B3BA1AEaDd3dCAa7aC7A37C1CBDA8A",
            chain_id="ethereum",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            contract = await response.parse()
            assert contract is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_source(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.evm.explorer.contract.with_raw_response.get_source(
                address="",
                chain_id="ethereum",
            )
