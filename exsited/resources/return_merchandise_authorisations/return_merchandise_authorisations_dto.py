"""Typed views over the return merchandise authorisation bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "ReturnMerchandiseAuthorisation",
    "ReturnMerchandiseAuthorisationList",
    "InvoiceReturnMerchandiseAuthorisationReceive",
    "InvoiceReturnMerchandiseAuthorisationReceiveList",
    "ReturnMerchandiseAuthorisationRead",
    "InvoiceReturnMerchandiseAuthorisations",
    "ReturnMerchandiseAuthorisations",
    "ReturnMerchandiseAuthorisationReadAccount",
    "ReturnMerchandiseAuthorisationReadSaleInvoice",
    "ReturnMerchandiseAuthorisationReadReceiveRma",
    "ReturnMerchandiseAuthorisationReadCreatedBy",
    "InvoiceReturnMerchandiseAuthorisationReceiveListData",
    "InvoiceReturnMerchandiseAuthorisationReceiveReceiveRma",
    "ReturnMerchandiseAuthorisationsReturnMerchandiseAuthorisation",
    "ReturnMerchandiseAuthorisationAccount",
    "ReturnMerchandiseAuthorisationSaleInvoice",
    "ReturnMerchandiseAuthorisationCreatedBy",
    "ReturnMerchandiseAuthorisationReadReceiveRmaCreatedBy",
    "InvoiceReturnMerchandiseAuthorisationReceiveListDataCreatedBy",
    "InvoiceReturnMerchandiseAuthorisationReceiveReceiveRmaCreatedBy",
]


class ReturnMerchandiseAuthorisation(Dto):
    """The return merchandise authorisation body."""

    MEASURED_FROM = ("GET /api/{api_version}/return_merchandise_authorisations",)

    account: ReturnMerchandiseAuthorisationAccount | None = None
    code: str | None = None
    created_by: ReturnMerchandiseAuthorisationCreatedBy | None = None
    created_on: str | None = None
    href: str | None = None
    id: str | None = None
    item_count: int | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    note: str | None = None
    object: str | None = None
    return_status: str | None = None
    rma_date: str | None = None
    sale_invoice: ReturnMerchandiseAuthorisationSaleInvoice | None = None
    # Null in every record measured, so untyped.
    sale_order: Any = None
    status: str | None = None
    version: int | None = None
    # Null in every record measured, so untyped.
    warehouse: Any = None


class ReturnMerchandiseAuthorisationList(Dto):
    """One page of ``ReturnMerchandiseAuthorisation`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/return_merchandise_authorisations",)

    data: list[ReturnMerchandiseAuthorisation] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class InvoiceReturnMerchandiseAuthorisationReceive(Dto):
    """The invoice return merchandise authorisation receive body, under
    ``receive_return_merchandise_authorisation``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/invoices/{invoice_id}/return_merchandise_authorisations/{rma_code}/receive",
        "GET /api/{api_version}/invoices/{invoice_id}/return_merchandise_authorisations/{rma_code}/receive/{receive_uuid}",
        "GET /api/{api_version}/return_merchandise_authorisations/{rma_code}/receive/{receive_uuid}",
    )

    ENVELOPE_KEY = "receive_return_merchandise_authorisation"

    created_by: str | None = None
    created_on: str | None = None
    id: str | None = None
    receive_returns: list[Any] | None = None
    receive_rma: InvoiceReturnMerchandiseAuthorisationReceiveReceiveRma | None = None
    uuid: str | None = None


class InvoiceReturnMerchandiseAuthorisationReceiveList(Dto):
    """One page of ``InvoiceReturnMerchandiseAuthorisationReceive`` records, under
    ``receive_return_merchandise_authorisations`` rather than ``data``; paged by offset."""

    MEASURED_FROM = (
        "GET /api/{api_version}/invoices/{invoice_id}/return_merchandise_authorisations/{rma_code}/receive",
        "GET /api/{api_version}/return_merchandise_authorisations/{rma_code}/receive",
    )

    receive_return_merchandise_authorisations: (
        list[InvoiceReturnMerchandiseAuthorisationReceive] | None
    ) = None
    pagination: Pagination | None = None
    data: list[InvoiceReturnMerchandiseAuthorisationReceiveListData] | None = None
    object: str | None = None
    url: str | None = None


class ReturnMerchandiseAuthorisationRead(Dto):
    """The return merchandise authorisation read body, under
    ``return_merchandise_authorisation``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/invoices/{invoice_id}/return_merchandise_authorisations/{rma_id}",
        "GET /api/{api_version}/return_merchandise_authorisations/{rma_id}",
    )

    ENVELOPE_KEY = "return_merchandise_authorisation"

    account: ReturnMerchandiseAuthorisationReadAccount | None = None
    code: str | None = None
    created_by: ReturnMerchandiseAuthorisationReadCreatedBy | None = None
    created_on: str | None = None
    href: str | None = None
    id: str | None = None
    item_count: int | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    lines: list[Any] | None = None
    note: str | None = None
    object: str | None = None
    receive_rmas: list[ReturnMerchandiseAuthorisationReadReceiveRma] | None = None
    return_status: str | None = None
    rma_date: str | None = None
    sale_invoice: ReturnMerchandiseAuthorisationReadSaleInvoice | None = None
    # Null in every record measured, so untyped.
    sale_order: Any = None
    status: str | None = None
    version: int | None = None
    # Null in every record measured, so untyped.
    warehouse: Any = None


class InvoiceReturnMerchandiseAuthorisations(Dto):
    """The invoice return merchandise authorisations body."""

    MEASURED_FROM = (
        "GET /api/{api_version}/invoices/{invoice_id}/return_merchandise_authorisations",
    )

    data: list[ReturnMerchandiseAuthorisation] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class ReturnMerchandiseAuthorisations(Dto):
    """The return merchandise authorisations body, under ``invoice``."""

    MEASURED_FROM = ("POST /api/{api_version}/return_merchandise_authorisations",)

    ENVELOPE_KEY = "invoice"

    return_merchandise_authorisation: (
        ReturnMerchandiseAuthorisationsReturnMerchandiseAuthorisation | None
    ) = None


class ReturnMerchandiseAuthorisationReadAccount(Dto):
    """A :class:`ReturnMerchandiseAuthorisationRead`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ReturnMerchandiseAuthorisationReadSaleInvoice(Dto):
    """A :class:`ReturnMerchandiseAuthorisationRead`'s ``sale_invoice``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class ReturnMerchandiseAuthorisationReadReceiveRma(Dto):
    """One entry of a :class:`ReturnMerchandiseAuthorisationRead`'s ``receive_rmas``."""

    code: str | None = None
    created_by: ReturnMerchandiseAuthorisationReadReceiveRmaCreatedBy | None = None
    created_on: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    object: str | None = None
    quantity_received: float | None = None
    status: str | None = None


class ReturnMerchandiseAuthorisationReadCreatedBy(Dto):
    """A :class:`ReturnMerchandiseAuthorisationRead`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class InvoiceReturnMerchandiseAuthorisationReceiveListData(Dto):
    """One entry of a :class:`InvoiceReturnMerchandiseAuthorisationReceiveList`'s ``data``."""

    code: str | None = None
    created_by: InvoiceReturnMerchandiseAuthorisationReceiveListDataCreatedBy | None = None
    created_on: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    object: str | None = None
    quantity_received: float | None = None
    status: str | None = None


class InvoiceReturnMerchandiseAuthorisationReceiveReceiveRma(Dto):
    """A :class:`InvoiceReturnMerchandiseAuthorisationReceive`'s ``receive_rma``."""

    code: str | None = None
    created_by: InvoiceReturnMerchandiseAuthorisationReceiveReceiveRmaCreatedBy | None = None
    created_on: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    object: str | None = None
    quantity_received: float | None = None
    status: str | None = None


class ReturnMerchandiseAuthorisationsReturnMerchandiseAuthorisation(Dto):
    """A :class:`ReturnMerchandiseAuthorisations`'s ``return_merchandise_authorisation``."""

    activity_logs: list[Any] | None = None
    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None
    status: str | None = None
    version: int | None = None


class ReturnMerchandiseAuthorisationAccount(Dto):
    """A :class:`ReturnMerchandiseAuthorisation`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ReturnMerchandiseAuthorisationSaleInvoice(Dto):
    """A :class:`ReturnMerchandiseAuthorisation`'s ``sale_invoice``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class ReturnMerchandiseAuthorisationCreatedBy(Dto):
    """A :class:`ReturnMerchandiseAuthorisation`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class ReturnMerchandiseAuthorisationReadReceiveRmaCreatedBy(Dto):
    """A :class:`ReturnMerchandiseAuthorisationReadReceiveRma`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class InvoiceReturnMerchandiseAuthorisationReceiveListDataCreatedBy(Dto):
    """A :class:`InvoiceReturnMerchandiseAuthorisationReceiveListData`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class InvoiceReturnMerchandiseAuthorisationReceiveReceiveRmaCreatedBy(Dto):
    """A :class:`InvoiceReturnMerchandiseAuthorisationReceiveReceiveRma`'s ``created_by``."""

    name: str | None = None
    object: str | None = None
