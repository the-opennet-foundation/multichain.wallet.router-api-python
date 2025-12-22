# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["JupiterSwapParams"]


class JupiterSwapParams(TypedDict, total=False):
    quote_response: Required[Annotated[object, PropertyInfo(alias="quoteResponse")]]
    """Quote response from /jupiter/quote"""

    user_public_key: Required[Annotated[str, PropertyInfo(alias="userPublicKey")]]
    """User wallet public key"""
