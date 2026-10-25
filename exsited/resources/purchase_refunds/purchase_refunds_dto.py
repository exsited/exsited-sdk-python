"""Typed views over the purchase refund bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "PurchaseRefunds",
    "PurchaseRefund",
    "AccountPurchaseRefunds",
    "AccountPurchaseRefundsData",
    "PurchaseRefundsData",
    "PurchaseRefundAccount",
    "PurchaseRefundCreditNote",
    "PurchaseRefundCustomAttribute",
    "PurchaseRefundCreatedBy",
    "AccountPurchaseRefundsDataDetail",
    "AccountPurchaseRefundsDataCreditNote",
    "AccountPurchaseRefundsDataCustomAttribute",
    "AccountPurchaseRefundsDataCreatedBy",
    "PurchaseRefundsDataAccount",
    "PurchaseRefundsDataCreditNote",
    "PurchaseRefundsDataCustomAttribute",
    "PurchaseRefundsDataCreatedBy",
]


class PurchaseRefunds(Dto):
    """The purchase refunds body."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_refunds",)

    alternate_date: str | None = None
    amount: str | None = None
    created_by: str | None = None
    created_on: str | None = None
    credit_note_id: str | None = None
    custom_attributes: list[Any] | None = None
    data: list[PurchaseRefundsData] | None = None
    date: str | None = None
    id: str | None = None
    last_updated_by: str | None = None
    last_updated_on: str | None = None
    note: str | None = None
    object: str | None = None
    pagination: Pagination | None = None
    payment_method: str | None = None
    payment_processor: str | None = None
    reference: str | None = None
    status: str | None = None
    url: str | None = None
    uuid: str | None = None
    version: str | None = None


class PurchaseRefund(Dto):
    """The purchase refund body, under ``purchase_refund``."""

    MEASURED_FROM = ("GET /api/{api_version}/purchase_refunds/{purchase_refund_id}",)

    ENVELOPE_KEY = "purchase_refund"

    account: PurchaseRefundAccount | None = None
    alternate_date: str | None = None
    amount: str | None = None
    created_by: PurchaseRefundCreatedBy | None = None
    created_on: str | None = None
    credit_note: PurchaseRefundCreditNote | None = None
    credit_note_id: str | None = None
    custom_attributes: list[PurchaseRefundCustomAttribute] | None = None
    date: str | None = None
    id: str | None = None
    issue_date: str | None = None
    last_updated_by: str | None = None
    last_updated_on: str | None = None
    note: str | None = None
    object: str | None = None
    payment_method: str | None = None
    payment_processor: str | None = None
    # Null in every record measured, so untyped.
    purchase_refund: Any = None
    reference: str | None = None
    status: str | None = None
    uuid: str | None = None
    version: int | None = None


class AccountPurchaseRefunds(Dto):
    """The account purchase refunds body."""

    MEASURED_FROM = ("GET /api/{api_version}/accounts/{account_id}/purchase_refunds",)

    data: list[AccountPurchaseRefundsData] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class AccountPurchaseRefundsData(Dto):
    """One entry of a :class:`AccountPurchaseRefunds`'s ``data``."""

    account: AccountPurchaseRefundsDataDetail | None = None
    amount: str | None = None
    created_by: AccountPurchaseRefundsDataCreatedBy | None = None
    created_on: str | None = None
    credit_note: AccountPurchaseRefundsDataCreditNote | None = None
    custom_attributes: list[AccountPurchaseRefundsDataCustomAttribute] | None = None
    id: str | None = None
    issue_date: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    note: str | None = None
    object: str | None = None
    payment_method: str | None = None
    payment_processor: str | None = None
    reference: str | None = None
    status: str | None = None
    uuid: str | None = None
    version: int | None = None


class PurchaseRefundsData(Dto):
    """One entry of a :class:`PurchaseRefunds`'s ``data``."""

    account: PurchaseRefundsDataAccount | None = None
    amount: str | None = None
    created_by: PurchaseRefundsDataCreatedBy | None = None
    created_on: str | None = None
    credit_note: PurchaseRefundsDataCreditNote | None = None
    custom_attributes: list[PurchaseRefundsDataCustomAttribute] | None = None
    id: str | None = None
    issue_date: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    note: str | None = None
    object: str | None = None
    payment_method: str | None = None
    payment_processor: str | None = None
    reference: str | None = None
    status: str | None = None
    uuid: str | None = None
    version: int | None = None


class PurchaseRefundAccount(Dto):
    """A :class:`PurchaseRefund`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseRefundCreditNote(Dto):
    """A :class:`PurchaseRefund`'s ``credit_note``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseRefundCustomAttribute(Dto):
    """One entry of a :class:`PurchaseRefund`'s ``custom_attributes``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    type: str | None = None
    value: str | None = None


class PurchaseRefundCreatedBy(Dto):
    """A :class:`PurchaseRefund`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class AccountPurchaseRefundsDataDetail(Dto):
    """A :class:`AccountPurchaseRefundsData`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class AccountPurchaseRefundsDataCreditNote(Dto):
    """A :class:`AccountPurchaseRefundsData`'s ``credit_note``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class AccountPurchaseRefundsDataCustomAttribute(Dto):
    """One entry of a :class:`AccountPurchaseRefundsData`'s ``custom_attributes``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    type: str | None = None
    value: str | None = None


class AccountPurchaseRefundsDataCreatedBy(Dto):
    """A :class:`AccountPurchaseRefundsData`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class PurchaseRefundsDataAccount(Dto):
    """A :class:`PurchaseRefundsData`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseRefundsDataCreditNote(Dto):
    """A :class:`PurchaseRefundsData`'s ``credit_note``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class PurchaseRefundsDataCustomAttribute(Dto):
    """One entry of a :class:`PurchaseRefundsData`'s ``custom_attributes``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    type: str | None = None
    value: str | None = None


class PurchaseRefundsDataCreatedBy(Dto):
    """A :class:`PurchaseRefundsData`'s ``created_by``."""

    name: str | None = None
    object: str | None = None
