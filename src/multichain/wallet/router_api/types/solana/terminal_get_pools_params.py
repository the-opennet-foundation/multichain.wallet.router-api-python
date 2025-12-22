# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TerminalGetPoolsParams"]


class TerminalGetPoolsParams(TypedDict, total=False):
    asset_ids: Required[Annotated[str, PropertyInfo(alias="assetIds")]]
    """Comma-separated mint addresses"""
