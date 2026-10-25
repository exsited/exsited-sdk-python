"""Typed views over the refund bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "Refund",
    "RefundList",
    "RefundUpdated",
    "AccountRefunds",
    "AccountRefundsData",
    "RefundAccount",
    "RefundCreditNote",
    "RefundUpdatedAccount",
    "RefundUpdatedCreditNote",
    "AccountRefundsDataDetail",
    "AccountRefundsDataCreditNote",
    "RefundNote",
    "RefundNoteList",
    "RefundNoteFile",
    "RefundNoteDetail",
    "RefundNoteAttachment",
    "RefundNoteWatcher",
    "RefundNoteCreatedBy",
]


class Refund(Dto):
    """The refund body, under ``refund``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/refunds",
        "GET /api/{api_version}/refunds/{refund_id}",
    )

    ENVELOPE_KEY = "refund"

    account: RefundAccount | None = None
    amount: str | None = None
    created_by: str | None = None
    created_on: str | None = None
    credit_note: RefundCreditNote | None = None
    custom_attributes: list[Any] | None = None
    # Null in every record measured, so untyped.
    gateway_response: Any = None
    id: str | None = None
    issue_date: str | None = None
    last_updated_by: str | None = None
    last_updated_on: str | None = None
    # Null in every record measured, so untyped.
    note: Any = None
    object: str | None = None
    payment_method: str | None = None
    payment_processor: str | None = None
    reconcile_status: str | None = None
    reference: str | None = None
    status: str | None = None
    uuid: str | None = None
    version: int | None = None


class RefundList(Dto):
    """One page of ``Refund`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/refunds",)

    data: list[Refund] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class RefundUpdated(Dto):
    """The refund updated body, under ``refund``."""

    MEASURED_FROM = (
        "POST /api/{api_version}/credit_notes/{credit_note_id}/refunds",
        "PATCH /api/{api_version}/refunds/{refund_id}",
    )

    ENVELOPE_KEY = "refund"

    account: RefundUpdatedAccount | None = None
    amount: str | None = None
    created_by: str | None = None
    created_on: str | None = None
    credit_note: RefundUpdatedCreditNote | None = None
    credit_note_id: str | None = None
    custom_attributes: list[Any] | None = None
    gateway_response: str | None = None
    id: str | None = None
    issue_date: str | None = None
    last_updated_by: str | None = None
    last_updated_on: str | None = None
    note: str | None = None
    object: str | None = None
    payment_method: str | None = None
    payment_processor: str | None = None
    reconcile_status: str | None = None
    reference: str | None = None
    status: str | None = None
    uuid: str | None = None
    version: int | None = None


class AccountRefunds(Dto):
    """The account refunds body."""

    MEASURED_FROM = ("GET /api/{api_version}/accounts/{account_id}/refunds",)

    data: list[AccountRefundsData] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class AccountRefundsData(Dto):
    """One entry of a :class:`AccountRefunds`'s ``data``."""

    account: AccountRefundsDataDetail | None = None
    amount: str | None = None
    created_by: str | None = None
    created_on: str | None = None
    credit_note: AccountRefundsDataCreditNote | None = None
    custom_attributes: list[Any] | None = None
    # Null in every record measured, so untyped.
    gateway_response: Any = None
    id: str | None = None
    issue_date: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    # Null in every record measured, so untyped.
    note: Any = None
    object: str | None = None
    payment_method: str | None = None
    payment_processor: str | None = None
    reconcile_status: str | None = None
    reference: str | None = None
    status: str | None = None
    uuid: str | None = None
    version: int | None = None


class RefundAccount(Dto):
    """A :class:`Refund`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class RefundCreditNote(Dto):
    """A :class:`Refund`'s ``credit_note``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class RefundUpdatedAccount(Dto):
    """A :class:`RefundUpdated`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class RefundUpdatedCreditNote(Dto):
    """A :class:`RefundUpdated`'s ``credit_note``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class AccountRefundsDataDetail(Dto):
    """A :class:`AccountRefundsData`'s ``account``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class AccountRefundsDataCreditNote(Dto):
    """A :class:`AccountRefundsData`'s ``credit_note``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class RefundNote(Dto):
    """One note on a refund, under ``note``."""

    MEASURED_FROM = (
        "POST /api/{api_version}/refunds/{refund_id}/notes",
        "GET /api/{api_version}/refunds/{refund_id}/notes",
        "GET /api/{api_version}/refunds/{refund_id}/notes/{note_id}",
    )

    ENVELOPE_KEY = "note"

    attachments: list[RefundNoteAttachment] | None = None
    content: str | None = None
    created_by: RefundNoteCreatedBy | None = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    group: Any = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    object: str | None = None
    refund: RefundNoteDetail | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[RefundNoteWatcher] | None = None


class RefundNoteList(Dto):
    """One page of ``RefundNote`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/refunds/{refund_id}/notes",)

    data: list[RefundNote] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class RefundNoteFile(Dto):
    """One attachment's descriptor, under ``file``."""

    MEASURED_FROM = ("GET /api/{api_version}/refunds/{refund_id}/notes/{note_id}/files/{file_id}",)

    ENVELOPE_KEY = "file"

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class RefundNoteDetail(Dto):
    """A :class:`RefundNote`'s ``refund``."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class RefundNoteAttachment(Dto):
    """One entry of a :class:`RefundNote`'s ``attachments``."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class RefundNoteWatcher(Dto):
    """One entry of a :class:`RefundNote`'s ``watchers``."""

    # Null in every record measured, so untyped.
    email: Any = None
    name: str | None = None
    type: str | None = None


class RefundNoteCreatedBy(Dto):
    """A :class:`RefundNote`'s ``created_by``."""

    name: str | None = None
    object: str | None = None
