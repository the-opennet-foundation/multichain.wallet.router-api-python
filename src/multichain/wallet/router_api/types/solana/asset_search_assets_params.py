# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AssetSearchAssetsParams", "Grouping"]


class AssetSearchAssetsParams(TypedDict, total=False):
    burnt: bool

    creator_address: Annotated[str, PropertyInfo(alias="creatorAddress")]

    frozen: bool

    grouping: Iterable[Grouping]

    limit: int

    owner_address: Annotated[str, PropertyInfo(alias="ownerAddress")]

    page: int


class Grouping(TypedDict, total=False):
    group_key: str

    group_value: str
