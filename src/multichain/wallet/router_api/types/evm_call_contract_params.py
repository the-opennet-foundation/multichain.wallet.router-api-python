# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EvmCallContractParams", "Transaction"]


class EvmCallContractParams(TypedDict, total=False):
    block_tag: Annotated[str, PropertyInfo(alias="blockTag")]

    transaction: Transaction


class Transaction(TypedDict, total=False):
    data: str

    to: str
