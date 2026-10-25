"""Child organisation endpoints, under ``/api/{api_version}/settings/organisations``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.organisations import organisations_urls

__all__ = [
    "get_settings_organisations",
    "create_settings_organisation",
    "get_settings_organisation",
    "delete_settings_organisation",
    "update_settings_organisation",
]

OrganisationPayload = Mapping[str, Any] | str | Dto


def get_settings_organisations(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """List the child organisations - ``GET /settings/organisations``; the root is never among
    them."""
    return client.send_get_request(
        organisations_urls.SETTINGS_ORGANISATIONS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_settings_organisation(
    client: Any,
    payload: OrganisationPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Create a child organisation - ``POST /settings/organisations``; the envelope is
    ``organization``, with a z."""
    _require_payload(payload)
    return client.send_post_request(
        organisations_urls.SETTINGS_ORGANISATIONS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_settings_organisation(
    client: Any,
    organisation_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Get one organisation - ``GET /settings/organisations/{organisation_id}``."""
    return client.send_get_request(
        organisations_urls.SETTINGS_ORGANISATION,
        path_params={"organisation_id": organisation_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_settings_organisation(
    client: Any,
    organisation_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete an organisation - ``DELETE /settings/organisations/{organisation_id}``."""
    return client.send_delete_request(
        organisations_urls.SETTINGS_ORGANISATION,
        path_params={"organisation_id": organisation_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_organisation(
    client: Any,
    organisation_id: str,
    payload: OrganisationPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update an organisation - ``PATCH /settings/organisations/{organisation_id}``."""
    _require_payload(payload)
    return client.send_patch_request(
        organisations_urls.SETTINGS_ORGANISATION,
        path_params={"organisation_id": organisation_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
