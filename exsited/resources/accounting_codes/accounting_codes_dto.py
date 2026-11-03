"""Typed views over the accounting code bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsAccountingCode",
    "SettingsAccountingCodeList",
]


class SettingsAccountingCode(Dto):
    """The settings accounting code body, under ``accounting_code``."""


    ENVELOPE_KEY = "accounting_code"

    account_code_type: str | None = None
    created_by: Any = None
    created_on: str | None = None
    default_match_key: str | None = None
    description: Any = None
    display_name: str | None = None
    gl_account_name: str | None = None
    gl_account_number: str | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    status: str | None = None
    version: int | None = None


class SettingsAccountingCodeList(Dto):
    """One page of ``SettingsAccountingCode`` records, under ``data``."""


    data: list[SettingsAccountingCode] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
