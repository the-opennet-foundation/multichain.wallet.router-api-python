# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BitcoinGetUtxoParams"]


class BitcoinGetUtxoParams(TypedDict, total=False):
    txid: Required[str]

    include_mempool: Annotated[bool, PropertyInfo(alias="includeMempool")]
