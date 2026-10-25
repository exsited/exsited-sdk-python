"""Accounting code endpoints, under ``/api/{api_version}/settings/accounting_codes``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.accounting_codes import accounting_codes_urls
from exsited.resources.accounting_codes.accounting_codes_dto import (
    SettingsAccountingCode,
    SettingsAccountingCodeList,
)

__all__ = [
    "get_settings_accounting_codes",
    "create_settings_accounting_code",
    "get_settings_accounting_code",
    "delete_settings_accounting_code",
    "update_settings_accounting_code",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

AccountingCodePayload = Mapping[str, Any] | str | Dto


def get_settings_accounting_codes(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsAccountingCodeList]:
    """List all - ``GET /settings/accounting_codes``."""
    return client.send_get_request(
        accounting_codes_urls.SETTINGS_ACCOUNTING_CODES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsAccountingCodeList,
    )


def create_settings_accounting_code(
    client: Any,
    payload: AccountingCodePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsAccountingCode]:
    """Create accounting code - ``POST /settings/accounting_codes``."""
    _require_payload(payload)
    return client.send_post_request(
        accounting_codes_urls.SETTINGS_ACCOUNTING_CODES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsAccountingCode,
    )


def get_settings_accounting_code(
    client: Any,
    accounting_code_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsAccountingCode]:
    """Get single - ``GET /settings/accounting_codes/{accounting_code_id}``."""
    return client.send_get_request(
        accounting_codes_urls.SETTINGS_ACCOUNTING_CODE,
        path_params={"accounting_code_id": accounting_code_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsAccountingCode,
    )


def delete_settings_accounting_code(
    client: Any,
    accounting_code_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete accounting code - ``DELETE /settings/accounting_codes/{accounting_code_id}``."""
    return client.send_delete_request(
        accounting_codes_urls.SETTINGS_ACCOUNTING_CODE,
        path_params={"accounting_code_id": accounting_code_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_accounting_code(
    client: Any,
    accounting_code_id: str,
    payload: AccountingCodePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsAccountingCode]:
    """Update accounting code - ``PATCH /settings/accounting_codes/{accounting_code_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        accounting_codes_urls.SETTINGS_ACCOUNTING_CODE,
        path_params={"accounting_code_id": accounting_code_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsAccountingCode,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
