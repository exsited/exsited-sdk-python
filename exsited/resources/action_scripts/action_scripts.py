"""Action script endpoints, under ``/api/{api_version}/action_scripts``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.action_scripts import action_scripts_urls
from exsited.resources.action_scripts.action_scripts_dto import ActionScript, ActionScriptList

__all__ = [
    "get_action_scripts",
    "get_action_script",
    "create_action_script",
    "update_action_script",
    "delete_action_script",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

ActionScriptPayload = Mapping[str, Any] | str | Dto


def get_action_scripts(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ActionScriptList]:
    """List action scripts - ``GET /action_scripts``; deleted scripts are left out."""
    return client.send_get_request(
        action_scripts_urls.ACTION_SCRIPTS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ActionScriptList,
    )


def get_action_script(
    client: Any,
    action_script_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ActionScript]:
    """One action script - ``GET /action_scripts/{action_script_id}``; the id is the ``ascr_``
    one."""
    return client.send_get_request(
        action_scripts_urls.ACTION_SCRIPT,
        path_params={"action_script_id": action_script_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ActionScript,
    )


def create_action_script(
    client: Any,
    payload: ActionScriptPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ActionScript]:
    """Store an action script - ``POST /action_scripts``, under ``action_script``; ``name`` is
    required and unique, and a ``script_file`` is a ``.js`` file sent as base64 ``content``."""
    _require_payload(payload)
    return client.send_post_request(
        action_scripts_urls.ACTION_SCRIPTS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ActionScript,
    )


def update_action_script(
    client: Any,
    action_script_id: str,
    payload: ActionScriptPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ActionScript]:
    """Update an action script - ``PATCH /action_scripts/{action_script_id}``, under
    ``action_script``; an unknown key is refused."""
    _require_payload(payload)
    return client.send_patch_request(
        action_scripts_urls.ACTION_SCRIPT,
        path_params={"action_script_id": action_script_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ActionScript,
    )


def delete_action_script(
    client: Any,
    action_script_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete an action script - ``DELETE /action_scripts/{action_script_id}``; answered
    ``204``."""
    return client.send_delete_request(
        action_scripts_urls.ACTION_SCRIPT,
        path_params={"action_script_id": action_script_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
