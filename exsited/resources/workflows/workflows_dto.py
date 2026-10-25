"""Typed views over the workflow bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "WorkflowList",
    "Workflow",
    "WorkflowView",
    "WorkflowCurrentVersion",
    "WorkflowCreatedBy",
    "WorkflowLastUpdatedBy",
    "WorkflowMilestoneView",
    "WorkflowMilestoneList",
    "WorkflowMilestone",
    "WorkflowMilestoneDetail",
    "WorkflowMilestoneActivityDefinition",
    "WorkflowMilestoneWorkflowVersion",
]


class WorkflowList(Dto):
    """One page of what ``get_workflows`` lists, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/workflows",)

    data: list[Workflow] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class Workflow(Dto):
    """One entry of a :class:`WorkflowList`'s ``data``."""

    object: str | None = None
    id: str | None = None
    status: str | None = None
    # Null in every record measured, so untyped.
    code: Any = None
    name: str | None = None
    display_name: str | None = None
    # Null in every record measured, so untyped.
    description: Any = None
    entity: str | None = None
    entity_id: int | None = None
    event: str | None = None
    is_pre_built: bool | None = None
    enable_stage: bool | None = None
    current_version: WorkflowCurrentVersion | None = None
    # Null in every record measured, so untyped.
    custom_form: Any = None
    created_on: str | None = None
    last_updated_on: str | None = None
    created_by: WorkflowCreatedBy | None = None
    last_updated_by: WorkflowLastUpdatedBy | None = None
    href: str | None = None


class WorkflowView(Workflow):
    """One workflow, under ``workflow``: what ``get_workflow`` answers, and the create and the
    update, which the handler answers through the same read."""

    MEASURED_FROM = ("GET /api/{api_version}/workflows/{workflow_id}",)

    ENVELOPE_KEY = "workflow"


class WorkflowCurrentVersion(Dto):
    """A :class:`Workflow`'s ``current_version``."""

    object: str | None = None
    id: str | None = None
    name: str | None = None


class WorkflowCreatedBy(Dto):
    """A :class:`Workflow`'s ``created_by``."""

    object: str | None = None
    name: str | None = None


class WorkflowLastUpdatedBy(Dto):
    """A :class:`Workflow`'s ``last_updated_by``."""

    object: str | None = None
    name: str | None = None


class WorkflowMilestoneList(Dto):
    """One page of what ``get_workflow_milestones`` lists, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/workflows/{workflow_uuid}/milestones",)

    data: list[WorkflowMilestone] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class WorkflowMilestone(Dto):
    """One entry of a :class:`WorkflowMilestoneList`'s ``data``."""

    activity_definition: WorkflowMilestoneActivityDefinition | None = None
    # Null in every record measured, so untyped.
    auto_create: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    description: Any = None
    display_name: str | None = None
    # Null in every record measured, so untyped.
    estimated_hours: Any = None
    href: str | None = None
    # Null in every record measured, so untyped.
    icon: Any = None
    id: str | None = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    priority: str | None = None
    # Null in every record measured, so untyped.
    sort_order: Any = None
    status: str | None = None
    workflow: WorkflowMilestoneDetail | None = None
    workflow_version: WorkflowMilestoneWorkflowVersion | None = None


class WorkflowMilestoneView(WorkflowMilestone):
    """One milestone definition, under ``workflow_milestone``: what ``get_workflow_milestone``
    answers, the same fields as a listed one."""

    MEASURED_FROM = ("GET /api/{api_version}/workflows/{workflow_id}/milestones/{milestone_id}",)

    ENVELOPE_KEY = "workflow_milestone"


class WorkflowMilestoneDetail(Dto):
    """A :class:`WorkflowMilestone`'s ``workflow``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class WorkflowMilestoneActivityDefinition(Dto):
    """A :class:`WorkflowMilestone`'s ``activity_definition``."""

    id: str | None = None
    name: str | None = None
    object: str | None = None


class WorkflowMilestoneWorkflowVersion(Dto):
    """A :class:`WorkflowMilestone`'s ``workflow_version``."""

    id: str | None = None
    name: str | None = None
    object: str | None = None
