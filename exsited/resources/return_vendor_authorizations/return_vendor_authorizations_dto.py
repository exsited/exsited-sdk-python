"""Typed views over the return vendor authorization bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "ReturnVendorAuthorization",
    "ReturnVendorAuthorizationList",
    "ReturnVendorAuthorizationView",
    "ReturnVendorAuthorizationAccount",
    "ReturnVendorAuthorizationPurchaseOrder",
    "ReturnVendorAuthorizationCreatedBy",
]


class ReturnVendorAuthorization(Dto):
    """One return vendor authorization, as the listing returns it."""

    MEASURED_FROM = ("GET /api/{api_version}/return_vendor_authorizations",)

    account: ReturnVendorAuthorizationAccount | None = None
    code: str | None = None
    created_by: ReturnVendorAuthorizationCreatedBy | None = None
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
    purchase_order: ReturnVendorAuthorizationPurchaseOrder | None = None
    return_status: str | None = None
    rva_date: str | None = None
    status: str | None = None
    version: int | None = None


class ReturnVendorAuthorizationList(Dto):
    """One page of ``ReturnVendorAuthorization`` records, under ``data``; paged by cursor."""

    MEASURED_FROM = ("GET /api/{api_version}/return_vendor_authorizations",)

    data: list[ReturnVendorAuthorization] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class ReturnVendorAuthorizationView(ReturnVendorAuthorization):
    """What ``get_return_vendor_authorization`` answers, under ``return_vendor_authorization``:
    the listing's record with its ``lines`` and ``receive_rvas``."""

    MEASURED_FROM = ("GET /api/{api_version}/return_vendor_authorizations/{rva_id}",)

    ENVELOPE_KEY = "return_vendor_authorization"

    # Empty in every record measured, so the entries are untyped.
    lines: list[Any] | None = None
    # Empty in every record measured, so the entries are untyped.
    receive_rvas: list[Any] | None = None


class ReturnVendorAuthorizationAccount(Dto):
    """A :class:`ReturnVendorAuthorization`'s ``account``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ReturnVendorAuthorizationPurchaseOrder(Dto):
    """A :class:`ReturnVendorAuthorization`'s ``purchase_order``."""

    code: str | None = None
    href: str | None = None
    id: str | None = None
    object: str | None = None


class ReturnVendorAuthorizationCreatedBy(Dto):
    """A :class:`ReturnVendorAuthorization`'s ``created_by``."""

    name: str | None = None
    object: str | None = None
