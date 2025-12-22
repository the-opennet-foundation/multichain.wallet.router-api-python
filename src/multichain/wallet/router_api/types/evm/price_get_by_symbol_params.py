# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["PriceGetBySymbolParams"]


class PriceGetBySymbolParams(TypedDict, total=False):
    symbols: SequenceNotStr[str]
