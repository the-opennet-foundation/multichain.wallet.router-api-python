# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["TxGetPaginatedParams"]


class TxGetPaginatedParams(TypedDict, total=False):
    last_seen_txid: Annotated[str, PropertyInfo(alias="lastSeenTxid")]
    """Last seen txid for pagination"""
