"""Receive term endpoints, under ``/api/{api_version}/settings/receive_terms``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.receive_terms import receive_terms_urls
from exsited.resources.receive_terms.receive_terms_dto import (
    SettingsReceiveTerm,
    SettingsReceiveTermList,
)

__all__ = [
    "get_settings_receive_terms",
    "create_settings_receive_term",
    "get_settings_receive_term",
    "delete_settings_receive_term",
    "update_settings_receive_term",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

ReceiveTermPayload = Mapping[str, Any] | str | Dto


def get_settings_receive_terms(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsReceiveTermList]:
    """List receive terms - ``GET /settings/receive_terms``."""
    return client.send_get_request(
        receive_terms_urls.SETTINGS_RECEIVE_TERMS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsReceiveTermList,
    )


def create_settings_receive_term(
    client: Any,
    payload: ReceiveTermPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsReceiveTerm]:
    """Create a receive term - ``POST /settings/receive_terms``; ``period`` is sent upper case
    and answered lower case."""
    _require_payload(payload)
    return client.send_post_request(
        receive_terms_urls.SETTINGS_RECEIVE_TERMS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsReceiveTerm,
    )


def get_settings_receive_term(
    client: Any,
    receive_term_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsReceiveTerm]:
    """Get one receive term - ``GET /settings/receive_terms/{receive_term_id}``."""
    return client.send_get_request(
        receive_terms_urls.SETTINGS_RECEIVE_TERM,
        path_params={"receive_term_id": receive_term_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsReceiveTerm,
    )


def delete_settings_receive_term(
    client: Any,
    receive_term_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a receive term - ``DELETE /settings/receive_terms/{receive_term_id}``."""
    return client.send_delete_request(
        receive_terms_urls.SETTINGS_RECEIVE_TERM,
        path_params={"receive_term_id": receive_term_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_receive_term(
    client: Any,
    receive_term_id: str,
    payload: ReceiveTermPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsReceiveTerm]:
    """Update or enable/disable a receive term - ``PATCH
    /settings/receive_terms/{receive_term_id}``; ``status`` takes active or inactive."""
    _require_payload(payload)
    return client.send_patch_request(
        receive_terms_urls.SETTINGS_RECEIVE_TERM,
        path_params={"receive_term_id": receive_term_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsReceiveTerm,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
