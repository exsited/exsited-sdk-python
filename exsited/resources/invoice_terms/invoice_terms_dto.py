"""Typed views over the invoice term bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsInvoiceTerm",
    "SettingsInvoiceTermList",
    "SettingsInvoiceTermDuration",
    "SettingsInvoiceTermWrite",
]


class SettingsInvoiceTerm(Dto):
    """The settings invoice term body, under ``invoice_term``."""


    ENVELOPE_KEY = "invoice_term"

    description: str | None = None
    display_name: str | None = None
    duration: SettingsInvoiceTermDuration | None = None
    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None


class SettingsInvoiceTermList(Dto):
    """One page of ``SettingsInvoiceTerm`` records, under ``data``."""


    data: list[SettingsInvoiceTerm] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class SettingsInvoiceTermDuration(Dto):
    """A :class:`SettingsInvoiceTerm`'s ``duration``."""

    count: int | None = None
    period: str | None = None


class SettingsInvoiceTermWrite(Dto):
    """The settings invoice term body a create or an update answers, under ``invoice_term``."""


    ENVELOPE_KEY = "invoice_term"

    created_by: Any = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    duration: int | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    ordering: int | None = None
    period: str | None = None
    status: str | None = None
