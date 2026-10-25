"""Typed views over the gift certificate bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "GiftCertificate",
    "GiftCertificateList",
    "GiftCertificateTransaction",
    "GiftCertificateTransactionList",
    "GiftCertificateAllocations",
    "GiftCertificateCurrency",
    "GiftCertificateAccountingCode",
    "GiftCertificateAllocation",
    "GiftCertificateActivityLog",
    "GiftCertificateAllocationsData",
    "GiftCertificateAllocationAccount",
    "GiftCertificateTransactionCurrency",
    "GiftCertificateTransactionAccountingCode",
    "GiftCertificateAllocationsDataAccount",
    "GiftCertificateAllocationRead",
    "GiftCertificateTransactionRead",
]


class GiftCertificate(Dto):
    """The gift certificate body, under ``gift_certificate``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/gift_certificates",
        "GET /api/{api_version}/gift_certificates/{gc_id}",
        "POST /api/{api_version}/gift_certificates",
        "PATCH /api/{api_version}/gift_certificates/{gc_id}",
    )

    ENVELOPE_KEY = "gift_certificate"

    accounting_code: GiftCertificateAccountingCode | None = None
    activity_logs: list[GiftCertificateActivityLog] | None = None
    allocations: list[GiftCertificateAllocation] | None = None
    amount: str | None = None
    code: str | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    currency: GiftCertificateCurrency | None = None
    expiry_date: str | None = None
    href: str | None = None
    id: str | None = None
    issue_date: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    # Null in every record measured, so untyped.
    linked_item: Any = None
    object: str | None = None
    remaining_balance: str | None = None
    status: str | None = None
    transactions: list[GiftCertificateTransaction] | None = None
    used_amount: str | None = None
    version: int | None = None


class GiftCertificateList(Dto):
    """One page of ``GiftCertificate`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/gift_certificates",)

    data: list[GiftCertificate] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class GiftCertificateTransaction(Dto):
    """The gift certificate transaction body."""

    MEASURED_FROM = ("GET /api/{api_version}/gift_certificates/{gc_id}/transactions",)

    accounting_code: GiftCertificateTransactionAccountingCode | None = None
    amount: str | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    currency: GiftCertificateTransactionCurrency | None = None
    date: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    object: str | None = None
    # Null in every record measured, so untyped.
    reference: Any = None
    status: str | None = None
    type: str | None = None
    version: int | None = None


class GiftCertificateTransactionList(Dto):
    """One page of ``GiftCertificateTransaction`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/gift_certificates/{gc_id}/transactions",)

    data: list[GiftCertificateTransaction] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class GiftCertificateAllocations(Dto):
    """The gift certificate allocations body."""

    MEASURED_FROM = ("GET /api/{api_version}/gift_certificates/{gc_id}/allocations",)

    data: list[GiftCertificateAllocationsData] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class GiftCertificateCurrency(Dto):
    """A :class:`GiftCertificate`'s ``currency``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class GiftCertificateAccountingCode(Dto):
    """A :class:`GiftCertificate`'s ``accounting_code``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class GiftCertificateAllocation(Dto):
    """One entry of a :class:`GiftCertificate`'s ``allocations``."""

    account: GiftCertificateAllocationAccount | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    date: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    object: str | None = None
    status: str | None = None
    type: str | None = None
    version: int | None = None


class GiftCertificateActivityLog(Dto):
    """One entry of a :class:`GiftCertificate`'s ``activity_logs``."""

    activity: str | None = None


class GiftCertificateAllocationsData(Dto):
    """One entry of a :class:`GiftCertificateAllocations`'s ``data``."""

    account: GiftCertificateAllocationsDataAccount | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    date: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    object: str | None = None
    status: str | None = None
    type: str | None = None
    version: int | None = None


class GiftCertificateAllocationAccount(Dto):
    """A :class:`GiftCertificateAllocation`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class GiftCertificateTransactionCurrency(Dto):
    """A :class:`GiftCertificateTransaction`'s ``currency``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class GiftCertificateTransactionAccountingCode(Dto):
    """A :class:`GiftCertificateTransaction`'s ``accounting_code``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class GiftCertificateAllocationsDataAccount(Dto):
    """A :class:`GiftCertificateAllocationsData`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class GiftCertificateAllocationRead(GiftCertificateAllocation):
    """One allocation, under ``gift_certificate_allocation``: the fields an allocation carries in
    ``allocations``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/gift_certificates/{gc_id}/allocations/{allocation_id}",
    )

    ENVELOPE_KEY = "gift_certificate_allocation"


class GiftCertificateTransactionRead(GiftCertificateTransaction):
    """One transaction, under ``gift_certificate_transaction``: the fields a transaction carries in
    ``transactions``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/gift_certificates/{gc_id}/transactions/{transaction_id}",
    )

    ENVELOPE_KEY = "gift_certificate_transaction"
