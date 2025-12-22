# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from multichain.wallet.router_api import MultichainWalletRouterAPI, AsyncMultichainWalletRouterAPI

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: MultichainWalletRouterAPI) -> None:
        asset = client.solana.assets.retrieve(
            "assetId",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.assets.with_raw_response.retrieve(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.assets.with_streaming_response.retrieve(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.solana.assets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_multiple_assets(self, client: MultichainWalletRouterAPI) -> None:
        asset = client.solana.assets.create_multiple_assets()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_multiple_assets_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        asset = client.solana.assets.create_multiple_assets(
            asset_ids=["string"],
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_multiple_assets(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.assets.with_raw_response.create_multiple_assets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_multiple_assets(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.assets.with_streaming_response.create_multiple_assets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_proof(self, client: MultichainWalletRouterAPI) -> None:
        asset = client.solana.assets.get_proof(
            "assetId",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_proof(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.assets.with_raw_response.get_proof(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_proof(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.assets.with_streaming_response.get_proof(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_proof(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.solana.assets.with_raw_response.get_proof(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_signatures(self, client: MultichainWalletRouterAPI) -> None:
        asset = client.solana.assets.get_signatures(
            asset_id="assetId",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_signatures_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        asset = client.solana.assets.get_signatures(
            asset_id="assetId",
            limit=0,
            page=0,
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_signatures(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.assets.with_raw_response.get_signatures(
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_signatures(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.assets.with_streaming_response.get_signatures(
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get_signatures(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            client.solana.assets.with_raw_response.get_signatures(
                asset_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_assets_by_authority(self, client: MultichainWalletRouterAPI) -> None:
        asset = client.solana.assets.list_assets_by_authority(
            authority="authority",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_assets_by_authority_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        asset = client.solana.assets.list_assets_by_authority(
            authority="authority",
            limit=0,
            page=0,
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_assets_by_authority(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.assets.with_raw_response.list_assets_by_authority(
            authority="authority",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_assets_by_authority(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.assets.with_streaming_response.list_assets_by_authority(
            authority="authority",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_assets_by_authority(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `authority` but received ''"):
            client.solana.assets.with_raw_response.list_assets_by_authority(
                authority="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_assets_by_creator(self, client: MultichainWalletRouterAPI) -> None:
        asset = client.solana.assets.list_assets_by_creator(
            creator="creator",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_assets_by_creator_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        asset = client.solana.assets.list_assets_by_creator(
            creator="creator",
            limit=0,
            page=0,
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_assets_by_creator(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.assets.with_raw_response.list_assets_by_creator(
            creator="creator",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_assets_by_creator(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.assets.with_streaming_response.list_assets_by_creator(
            creator="creator",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_assets_by_creator(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `creator` but received ''"):
            client.solana.assets.with_raw_response.list_assets_by_creator(
                creator="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_assets_by_group(self, client: MultichainWalletRouterAPI) -> None:
        asset = client.solana.assets.list_assets_by_group(
            group_value="groupValue",
            group_key="collection",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_assets_by_group_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        asset = client.solana.assets.list_assets_by_group(
            group_value="groupValue",
            group_key="collection",
            limit=0,
            page=0,
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_assets_by_group(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.assets.with_raw_response.list_assets_by_group(
            group_value="groupValue",
            group_key="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_assets_by_group(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.assets.with_streaming_response.list_assets_by_group(
            group_value="groupValue",
            group_key="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_assets_by_group(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_key` but received ''"):
            client.solana.assets.with_raw_response.list_assets_by_group(
                group_value="groupValue",
                group_key="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_value` but received ''"):
            client.solana.assets.with_raw_response.list_assets_by_group(
                group_value="",
                group_key="collection",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_owned_assets(self, client: MultichainWalletRouterAPI) -> None:
        asset = client.solana.assets.list_owned_assets(
            owner="owner",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_owned_assets_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        asset = client.solana.assets.list_owned_assets(
            owner="owner",
            limit=1000,
            page=0,
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_owned_assets(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.assets.with_raw_response.list_owned_assets(
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_owned_assets(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.assets.with_streaming_response.list_owned_assets(
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_owned_assets(self, client: MultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            client.solana.assets.with_raw_response.list_owned_assets(
                owner="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_assets(self, client: MultichainWalletRouterAPI) -> None:
        asset = client.solana.assets.search_assets()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_assets_with_all_params(self, client: MultichainWalletRouterAPI) -> None:
        asset = client.solana.assets.search_assets(
            burnt=True,
            creator_address="creatorAddress",
            frozen=True,
            grouping=[
                {
                    "group_key": "group_key",
                    "group_value": "group_value",
                }
            ],
            limit=0,
            owner_address="ownerAddress",
            page=0,
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search_assets(self, client: MultichainWalletRouterAPI) -> None:
        response = client.solana.assets.with_raw_response.search_assets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search_assets(self, client: MultichainWalletRouterAPI) -> None:
        with client.solana.assets.with_streaming_response.search_assets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        asset = await async_client.solana.assets.retrieve(
            "assetId",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.assets.with_raw_response.retrieve(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.assets.with_streaming_response.retrieve(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.solana.assets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_multiple_assets(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        asset = await async_client.solana.assets.create_multiple_assets()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_multiple_assets_with_all_params(
        self, async_client: AsyncMultichainWalletRouterAPI
    ) -> None:
        asset = await async_client.solana.assets.create_multiple_assets(
            asset_ids=["string"],
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_multiple_assets(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.assets.with_raw_response.create_multiple_assets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_multiple_assets(
        self, async_client: AsyncMultichainWalletRouterAPI
    ) -> None:
        async with async_client.solana.assets.with_streaming_response.create_multiple_assets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_proof(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        asset = await async_client.solana.assets.get_proof(
            "assetId",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_proof(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.assets.with_raw_response.get_proof(
            "assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_proof(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.assets.with_streaming_response.get_proof(
            "assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_proof(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.solana.assets.with_raw_response.get_proof(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_signatures(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        asset = await async_client.solana.assets.get_signatures(
            asset_id="assetId",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_signatures_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        asset = await async_client.solana.assets.get_signatures(
            asset_id="assetId",
            limit=0,
            page=0,
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_signatures(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.assets.with_raw_response.get_signatures(
            asset_id="assetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_signatures(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.assets.with_streaming_response.get_signatures(
            asset_id="assetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get_signatures(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `asset_id` but received ''"):
            await async_client.solana.assets.with_raw_response.get_signatures(
                asset_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_assets_by_authority(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        asset = await async_client.solana.assets.list_assets_by_authority(
            authority="authority",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_assets_by_authority_with_all_params(
        self, async_client: AsyncMultichainWalletRouterAPI
    ) -> None:
        asset = await async_client.solana.assets.list_assets_by_authority(
            authority="authority",
            limit=0,
            page=0,
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_assets_by_authority(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.assets.with_raw_response.list_assets_by_authority(
            authority="authority",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_assets_by_authority(
        self, async_client: AsyncMultichainWalletRouterAPI
    ) -> None:
        async with async_client.solana.assets.with_streaming_response.list_assets_by_authority(
            authority="authority",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_assets_by_authority(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `authority` but received ''"):
            await async_client.solana.assets.with_raw_response.list_assets_by_authority(
                authority="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_assets_by_creator(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        asset = await async_client.solana.assets.list_assets_by_creator(
            creator="creator",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_assets_by_creator_with_all_params(
        self, async_client: AsyncMultichainWalletRouterAPI
    ) -> None:
        asset = await async_client.solana.assets.list_assets_by_creator(
            creator="creator",
            limit=0,
            page=0,
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_assets_by_creator(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.assets.with_raw_response.list_assets_by_creator(
            creator="creator",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_assets_by_creator(
        self, async_client: AsyncMultichainWalletRouterAPI
    ) -> None:
        async with async_client.solana.assets.with_streaming_response.list_assets_by_creator(
            creator="creator",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_assets_by_creator(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `creator` but received ''"):
            await async_client.solana.assets.with_raw_response.list_assets_by_creator(
                creator="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_assets_by_group(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        asset = await async_client.solana.assets.list_assets_by_group(
            group_value="groupValue",
            group_key="collection",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_assets_by_group_with_all_params(
        self, async_client: AsyncMultichainWalletRouterAPI
    ) -> None:
        asset = await async_client.solana.assets.list_assets_by_group(
            group_value="groupValue",
            group_key="collection",
            limit=0,
            page=0,
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_assets_by_group(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.assets.with_raw_response.list_assets_by_group(
            group_value="groupValue",
            group_key="collection",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_assets_by_group(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.assets.with_streaming_response.list_assets_by_group(
            group_value="groupValue",
            group_key="collection",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_assets_by_group(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_key` but received ''"):
            await async_client.solana.assets.with_raw_response.list_assets_by_group(
                group_value="groupValue",
                group_key="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `group_value` but received ''"):
            await async_client.solana.assets.with_raw_response.list_assets_by_group(
                group_value="",
                group_key="collection",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_owned_assets(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        asset = await async_client.solana.assets.list_owned_assets(
            owner="owner",
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_owned_assets_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        asset = await async_client.solana.assets.list_owned_assets(
            owner="owner",
            limit=1000,
            page=0,
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_owned_assets(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.assets.with_raw_response.list_owned_assets(
            owner="owner",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_owned_assets(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.assets.with_streaming_response.list_owned_assets(
            owner="owner",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_owned_assets(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `owner` but received ''"):
            await async_client.solana.assets.with_raw_response.list_owned_assets(
                owner="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_assets(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        asset = await async_client.solana.assets.search_assets()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_assets_with_all_params(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        asset = await async_client.solana.assets.search_assets(
            burnt=True,
            creator_address="creatorAddress",
            frozen=True,
            grouping=[
                {
                    "group_key": "group_key",
                    "group_value": "group_value",
                }
            ],
            limit=0,
            owner_address="ownerAddress",
            page=0,
        )
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search_assets(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        response = await async_client.solana.assets.with_raw_response.search_assets()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert asset is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search_assets(self, async_client: AsyncMultichainWalletRouterAPI) -> None:
        async with async_client.solana.assets.with_streaming_response.search_assets() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert asset is None

        assert cast(Any, response.is_closed) is True
