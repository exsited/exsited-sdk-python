"""Workflow endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from typing import Any, Mapping

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.workflows import workflows_urls
from exsited.resources.workflows.workflows_dto import (
    WorkflowList,
    WorkflowMilestoneList,
    WorkflowMilestoneView,
    WorkflowView,
)

__all__ = [
    "get_workflows",
    "get_workflow",
    "create_workflow",
    "update_workflow",
    "delete_workflow",
    "get_workflow_stages",
    "get_workflow_stage",
    "get_workflow_milestones",
    "get_workflow_milestone",
    "delete_milestone",
    "get_workflow_custom_component_history",
    "get_workflow_custom_component_milestones",
    "get_workflow_custom_component_milestone",
    "get_workflow_component_history",
    "get_workflow_component_cc_instance_cc_milestone",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

WorkflowPayload = Mapping[str, Any] | str | Dto


def get_workflows(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[WorkflowList]:
    """List workflows - ``GET /workflows``, cursor paged; a deleted one is not listed."""
    return client.send_get_request(
        workflows_urls.WORKFLOWS,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=WorkflowList,
    )


def get_workflow(
    client: Any,
    workflow_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[WorkflowView]:
    """Retrieve one workflow - ``GET /workflows/{workflow_id}``, the ``wf_`` id or the ``code``,
    under ``workflow``."""
    return client.send_get_request(
        workflows_urls.WORKFLOW,
        path_params={"workflow_id": workflow_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=WorkflowView,
    )


def create_workflow(
    client: Any,
    payload: WorkflowPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[WorkflowView]:
    """Create a workflow, as a draft - ``POST /workflows``, wrapped in ``workflow``; ``name`` is
    required and any key but the eight the handler reads is refused."""
    _require_payload(payload)
    return client.send_post_request(
        workflows_urls.WORKFLOWS,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=WorkflowView,
    )


def update_workflow(
    client: Any,
    workflow_id: str,
    payload: WorkflowPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[WorkflowView]:
    """Update a workflow or move its status - ``PATCH /workflows/{workflow_id}``, wrapped in
    ``workflow``; ``DRAFT`` goes to ``ACTIVE``, and ``ACTIVE`` and ``INACTIVE`` to each other."""
    _require_payload(payload)
    return client.send_patch_request(
        workflows_urls.WORKFLOW,
        path_params={"workflow_id": workflow_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=WorkflowView,
    )


def delete_workflow(
    client: Any,
    workflow_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a workflow - ``DELETE /workflows/{workflow_id}``; answered ``204``. The record is
    kept as ``DELETED`` and reads ``404`` after; a pre-built workflow is refused."""
    return client.send_delete_request(
        workflows_urls.WORKFLOW,
        path_params={"workflow_id": workflow_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_workflow_stages(
    client: Any,
    workflow_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """List a workflow's stages - ``GET /workflows/{workflow_id}/stages``. No stage has been
    measured, so no typed view."""
    return client.send_get_request(
        workflows_urls.WORKFLOW_STAGES,
        path_params={"workflow_id": workflow_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_workflow_stage(
    client: Any,
    workflow_id: str,
    stage_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Retrieve one stage - ``GET /workflows/{workflow_id}/stages/{stage_id}``, the ``wfs_`` id,
    under ``workflow_stage``. No stage has been measured, so no typed view."""
    return client.send_get_request(
        workflows_urls.WORKFLOW_STAGE,
        path_params={"workflow_id": workflow_id, "stage_id": stage_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_workflow_milestones(
    client: Any,
    workflow_uuid: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[WorkflowMilestoneList]:
    """Get workflow milestones (V4) - ``GET /workflows/{workflow_uuid}/milestones``."""
    return client.send_get_request(
        workflows_urls.WORKFLOW_MILESTONES,
        path_params={"workflow_uuid": workflow_uuid},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=WorkflowMilestoneList,
    )


def get_workflow_milestone(
    client: Any,
    workflow_id: str,
    milestone_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[WorkflowMilestoneView]:
    """Retrieve one milestone definition -
    ``GET /workflows/{workflow_id}/milestones/{milestone_id}``, the ``wfm_`` id, under
    ``workflow_milestone``."""
    return client.send_get_request(
        workflows_urls.WORKFLOW_MILESTONE,
        path_params={"workflow_id": workflow_id, "milestone_id": milestone_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=WorkflowMilestoneView,
    )


def delete_milestone(
    client: Any,
    milestone_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete milestone (V4) - ``DELETE /milestones/{milestone_uuid}``."""
    return client.send_delete_request(
        workflows_urls.MILESTONE,
        path_params={"milestone_uuid": milestone_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_workflow_custom_component_history(
    client: Any,
    component_uuid: str,
    object_code: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Workflow history of one component instance -
    ``GET /workflows/custom_components/{component_uuid}/{object_code}/history``, the component's
    dashed uuid and the instance's ``code``. Measured empty only, so no typed view."""
    return client.send_get_request(
        workflows_urls.WORKFLOW_CUSTOM_COMPONENT_HISTORY,
        path_params={"component_uuid": component_uuid, "object_code": object_code},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_workflow_custom_component_milestones(
    client: Any,
    component_uuid: str,
    object_code: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Milestones of one component instance -
    ``GET /workflows/custom_components/{component_uuid}/{object_code}/milestones``, the
    component's dashed uuid and the instance's ``code``. Measured empty only, so no typed view."""
    return client.send_get_request(
        workflows_urls.WORKFLOW_CUSTOM_COMPONENT_MILESTONES,
        path_params={"component_uuid": component_uuid, "object_code": object_code},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_workflow_custom_component_milestone(
    client: Any,
    component_uuid: str,
    object_code: str,
    milestone_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """One milestone of one component instance -
    ``GET /workflows/custom_components/{component_uuid}/{object_code}/milestones/{milestone_id}``,
    the ``wfmi_`` id, under ``workflow_milestone_instance``. Never measured, so no typed view."""
    return client.send_get_request(
        workflows_urls.WORKFLOW_CUSTOM_COMPONENT_MILESTONE,
        path_params={
            "component_uuid": component_uuid,
            "object_code": object_code,
            "milestone_id": milestone_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_workflow_component_history(
    client: Any,
    component_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Workflow history of one component instance, by its code -
    ``GET /workflow/component/{component_object_id}/history``; answered under
    ``histories``."""
    return client.send_get_request(
        workflows_urls.WORKFLOW_COMPONENT_HISTORY,
        path_params={"component_object_id": component_object_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_workflow_component_cc_instance_cc_milestone(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Milestones of one component instance, by the component's uuid and the instance's
    code - ``GET /workflow/component/{component_uuid}/{component_object_id}/milestone``;
    answered under ``milestones``."""
    return client.send_get_request(
        workflows_urls.WORKFLOW_COMPONENT_CC_INSTANCE_CC_MILESTONE,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )
