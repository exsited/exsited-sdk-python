"""Fulfillment term endpoints, under ``/api/{api_version}/settings/fulfillment_terms``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.fulfillment_terms import fulfillment_terms_urls
from exsited.resources.fulfillment_terms.fulfillment_terms_dto import (
    SettingsFulfillmentTerm,
    SettingsFulfillmentTermList,
)

__all__ = [
    "get_settings_fulfillment_terms",
    "create_settings_fulfillment_term",
    "get_settings_fulfillment_term",
    "delete_settings_fulfillment_term",
    "update_settings_fulfillment_term",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

FulfillmentTermPayload = Mapping[str, Any] | str | Dto


def get_settings_fulfillment_terms(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsFulfillmentTermList]:
    """List fulfillment terms - ``GET /settings/fulfillment_terms``."""
    return client.send_get_request(
        fulfillment_terms_urls.SETTINGS_FULFILLMENT_TERMS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsFulfillmentTermList,
    )


def create_settings_fulfillment_term(
    client: Any,
    payload: FulfillmentTermPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsFulfillmentTerm]:
    """Create a fulfillment term - ``POST /settings/fulfillment_terms``; ``period`` is sent
    upper case and answered lower case."""
    _require_payload(payload)
    return client.send_post_request(
        fulfillment_terms_urls.SETTINGS_FULFILLMENT_TERMS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsFulfillmentTerm,
    )


def get_settings_fulfillment_term(
    client: Any,
    fulfillment_term_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsFulfillmentTerm]:
    """Get one fulfillment term - ``GET /settings/fulfillment_terms/{fulfillment_term_id}``."""
    return client.send_get_request(
        fulfillment_terms_urls.SETTINGS_FULFILLMENT_TERM,
        path_params={"fulfillment_term_id": fulfillment_term_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsFulfillmentTerm,
    )


def delete_settings_fulfillment_term(
    client: Any,
    fulfillment_term_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a fulfillment term - ``DELETE /settings/fulfillment_terms/{fulfillment_term_id}``."""
    return client.send_delete_request(
        fulfillment_terms_urls.SETTINGS_FULFILLMENT_TERM,
        path_params={"fulfillment_term_id": fulfillment_term_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_fulfillment_term(
    client: Any,
    fulfillment_term_id: str,
    payload: FulfillmentTermPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsFulfillmentTerm]:
    """Update or enable/disable a fulfillment term - ``PATCH
    /settings/fulfillment_terms/{fulfillment_term_id}``; ``status`` takes active or inactive."""
    _require_payload(payload)
    return client.send_patch_request(
        fulfillment_terms_urls.SETTINGS_FULFILLMENT_TERM,
        path_params={"fulfillment_term_id": fulfillment_term_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsFulfillmentTerm,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
