"""Zone endpoints, under ``/api/{api_version}/settings/zones``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.zones import zones_urls
from exsited.resources.zones.zones_dto import (
    SettingsZone,
    SettingsZoneList,
)

__all__ = [
    "get_settings_zones",
    "create_settings_zone",
    "get_settings_zone",
    "delete_settings_zone",
    "update_settings_zone",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

ZonePayload = Mapping[str, Any] | str | Dto


def get_settings_zones(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsZoneList]:
    """List zones - ``GET /settings/zones``."""
    return client.send_get_request(
        zones_urls.SETTINGS_ZONES,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsZoneList,
    )


def create_settings_zone(
    client: Any,
    payload: ZonePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsZone]:
    """Create a zone - ``POST /settings/zones``; ``country_list`` takes country ids, one at
    least."""
    _require_payload(payload)
    return client.send_post_request(
        zones_urls.SETTINGS_ZONES,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsZone,
    )


def get_settings_zone(
    client: Any,
    zone_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsZone]:
    """Get one zone - ``GET /settings/zones/{zone_id}``."""
    return client.send_get_request(
        zones_urls.SETTINGS_ZONE,
        path_params={"zone_id": zone_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsZone,
    )


def delete_settings_zone(
    client: Any,
    zone_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a zone - ``DELETE /settings/zones/{zone_id}``."""
    return client.send_delete_request(
        zones_urls.SETTINGS_ZONE,
        path_params={"zone_id": zone_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_settings_zone(
    client: Any,
    zone_id: str,
    payload: ZonePayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsZone]:
    """Update a zone - ``PATCH /settings/zones/{zone_id}``; answers ``200``
    and changes nothing."""
    _require_payload(payload)
    return client.send_patch_request(
        zones_urls.SETTINGS_ZONE,
        path_params={"zone_id": zone_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsZone,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
