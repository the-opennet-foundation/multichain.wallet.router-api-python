# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["FeeGetPriorityParams"]


class FeeGetPriorityParams(TypedDict, total=False):
    account_keys: Annotated[str, PropertyInfo(alias="accountKeys")]
    """Comma-separated account keys"""
