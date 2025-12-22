# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["TxTestMempoolParams"]


class TxTestMempoolParams(TypedDict, total=False):
    raw_txs: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="rawTxs")]]
    """Raw transaction hexes"""
