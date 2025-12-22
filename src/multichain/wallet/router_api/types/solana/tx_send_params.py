# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TxSendParams"]


class TxSendParams(TypedDict, total=False):
    signed_transaction: Required[Annotated[str, PropertyInfo(alias="signedTransaction")]]
    """Base64-encoded signed transaction"""
