# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBlock:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_best(self, client: MultichainWalletRouterAPI) -> None:
        block = client.bitcoin.block.get_best()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_best(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.block.with_raw_response.get_best()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_best(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.block.with_streaming_response.get_best() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_hash(self, client: MultichainWalletRouterAPI) -> None:
        block = client.bitcoin.block.get_by_hash(
            hash="hash",
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_hash_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        block = client.bitcoin.block.get_by_hash(
            hash="hash",
            verbosity=0,
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_by_hash(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.block.with_raw_response.get_by_hash(
            hash="hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_by_hash(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.block.with_streaming_response.get_by_hash(
            hash="hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_by_hash(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hash` but received ''"):
            client.bitcoin.block.with_raw_response.get_by_hash(
                hash="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_by_height(self, client: MultichainWalletRouterAPI) -> None:
        block = client.bitcoin.block.get_by_height(
            0,
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_by_height(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.block.with_raw_response.get_by_height(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_by_height(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.block.with_streaming_response.get_by_height(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_header(self, client: MultichainWalletRouterAPI) -> None:
        block = client.bitcoin.block.get_header(
            hash="hash",
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_header_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        block = client.bitcoin.block.get_header(
            hash="hash",
            verbose=True,
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_header(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.block.with_raw_response.get_header(
            hash="hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_header(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.block.with_streaming_response.get_header(
            hash="hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_header(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hash` but received ''"):
            client.bitcoin.block.with_raw_response.get_header(
                hash="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_stats(self, client: MultichainWalletRouterAPI) -> None:
        block = client.bitcoin.block.get_stats(
            "hash",
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_stats(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.block.with_raw_response.get_stats(
            "hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_stats(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.block.with_streaming_response.get_stats(
            "hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_stats(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hash` but received ''"):
            client.bitcoin.block.with_raw_response.get_stats(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_tip(self, client: MultichainWalletRouterAPI) -> None:
        block = client.bitcoin.block.get_tip()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_tip(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.block.with_raw_response.get_tip()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_tip(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.block.with_streaming_response.get_tip() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_transaction_ids(self, client: MultichainWalletRouterAPI) -> None:
        block = client.bitcoin.block.get_transaction_ids(
            "hash",
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_transaction_ids(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.block.with_raw_response.get_transaction_ids(
            "hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_transaction_ids(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.block.with_streaming_response.get_transaction_ids(
            "hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_transaction_ids(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hash` but received ''"):
            client.bitcoin.block.with_raw_response.get_transaction_ids(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_transactions(self, client: MultichainWalletRouterAPI) -> None:
        block = client.bitcoin.block.get_transactions(
            hash="hash",
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_transactions_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        block = client.bitcoin.block.get_transactions(
            hash="hash",
            start_index=0,
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_transactions(self, client: MultichainWalletRouterAPI) -> None:
        response = client.bitcoin.block.with_raw_response.get_transactions(
            hash="hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_transactions(self, client: MultichainWalletRouterAPI) -> None:
        with client.bitcoin.block.with_streaming_response.get_transactions(
            hash="hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_transactions(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hash` but received ''"):
            client.bitcoin.block.with_raw_response.get_transactions(
                hash="",
            )


class TestAsyncBlock:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_best(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        block = await async_client.bitcoin.block.get_best()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_best(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.block.with_raw_response.get_best()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_best(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.block.with_streaming_response.get_best() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_hash(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        block = await async_client.bitcoin.block.get_by_hash(
            hash="hash",
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_hash_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        block = await async_client.bitcoin.block.get_by_hash(
            hash="hash",
            verbosity=0,
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_by_hash(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.block.with_raw_response.get_by_hash(
            hash="hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_hash(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.block.with_streaming_response.get_by_hash(
            hash="hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_by_hash(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hash` but received ''"):
            await async_client.bitcoin.block.with_raw_response.get_by_hash(
                hash="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_by_height(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        block = await async_client.bitcoin.block.get_by_height(
            0,
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_by_height(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.block.with_raw_response.get_by_height(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_by_height(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.block.with_streaming_response.get_by_height(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_header(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        block = await async_client.bitcoin.block.get_header(
            hash="hash",
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_header_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        block = await async_client.bitcoin.block.get_header(
            hash="hash",
            verbose=True,
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_header(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.block.with_raw_response.get_header(
            hash="hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_header(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.block.with_streaming_response.get_header(
            hash="hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_header(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hash` but received ''"):
            await async_client.bitcoin.block.with_raw_response.get_header(
                hash="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_stats(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        block = await async_client.bitcoin.block.get_stats(
            "hash",
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_stats(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.block.with_raw_response.get_stats(
            "hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_stats(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.block.with_streaming_response.get_stats(
            "hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_stats(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hash` but received ''"):
            await async_client.bitcoin.block.with_raw_response.get_stats(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_tip(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        block = await async_client.bitcoin.block.get_tip()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_tip(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.block.with_raw_response.get_tip()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_tip(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.block.with_streaming_response.get_tip() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_transaction_ids(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        block = await async_client.bitcoin.block.get_transaction_ids(
            "hash",
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_transaction_ids(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.block.with_raw_response.get_transaction_ids(
            "hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_transaction_ids(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.block.with_streaming_response.get_transaction_ids(
            "hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_transaction_ids(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hash` but received ''"):
            await async_client.bitcoin.block.with_raw_response.get_transaction_ids(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_transactions(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        block = await async_client.bitcoin.block.get_transactions(
            hash="hash",
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_transactions_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        block = await async_client.bitcoin.block.get_transactions(
            hash="hash",
            start_index=0,
        )
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_transactions(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.bitcoin.block.with_raw_response.get_transactions(
            hash="hash",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert block is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_transactions(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.bitcoin.block.with_streaming_response.get_transactions(
            hash="hash",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert block is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_transactions(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hash` but received ''"):
            await async_client.bitcoin.block.with_raw_response.get_transactions(
                hash="",
            )
