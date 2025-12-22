# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTxs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_all(self, client: MultichainWalletRouterAPI) -> None:
        tx = client.bitcoin.address.txs.get_all(
            "address",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_all(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.address.txs.with_raw_response.get_all(
            "address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_all(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.address.txs.with_streaming_response.get_all(
            "address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_all(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.bitcoin.address.txs.with_raw_response.get_all(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_paginated(self, client: MultichainWalletRouterAPI) -> None:
        tx = client.bitcoin.address.txs.get_paginated(
            address="address",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_paginated_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        tx = client.bitcoin.address.txs.get_paginated(
            address="address",
            last_seen_txid="lastSeenTxid",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_paginated(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.address.txs.with_raw_response.get_paginated(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_paginated(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.address.txs.with_streaming_response.get_paginated(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_paginated(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            client.bitcoin.address.txs.with_raw_response.get_paginated(
                address="",
            )


class TestAsyncTxs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_all(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        tx = await async_client.bitcoin.address.txs.get_all(
            "address",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_all(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.address.txs.with_raw_response.get_all(
            "address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = await response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_all(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.address.txs.with_streaming_response.get_all(
            "address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = await response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_all(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.bitcoin.address.txs.with_raw_response.get_all(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_paginated(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        tx = await async_client.bitcoin.address.txs.get_paginated(
            address="address",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_paginated_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        tx = await async_client.bitcoin.address.txs.get_paginated(
            address="address",
            last_seen_txid="lastSeenTxid",
        )
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_paginated(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.address.txs.with_raw_response.get_paginated(
            address="address",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tx = await response.parse()
        assert tx is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_paginated(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.address.txs.with_streaming_response.get_paginated(
            address="address",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tx = await response.parse()
            assert tx is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_paginated(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `address` but received ''"):
            await async_client.bitcoin.address.txs.with_raw_response.get_paginated(
                address="",
            )
