"""Settings workflow endpoints, under ``/api/{api_version}/settings/workflows``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.resources.settings_workflows import settings_workflows_urls
from exsited.resources.settings_workflows.settings_workflows_dto import (
    SettingsWorkflow,
    SettingsWorkflowList,
)

__all__ = [
    "get_settings_workflows",
    "get_settings_workflow",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"


def get_settings_workflows(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsWorkflowList]:
    """List workflows - ``GET /settings/workflows``; read only here, the writes live under
    ``/workflows``."""
    return client.send_get_request(
        settings_workflows_urls.SETTINGS_WORKFLOWS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsWorkflowList,
    )


def get_settings_workflow(
    client: Any,
    workflow_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[SettingsWorkflow]:
    """Get one workflow - ``GET /settings/workflows/{workflow_id}``."""
    return client.send_get_request(
        settings_workflows_urls.SETTINGS_WORKFLOW,
        path_params={"workflow_id": workflow_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=SettingsWorkflow,
    )
