"""Typed views over the task bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "Task",
    "TaskList",
    "TaskView",
    "TaskNoteList",
    "TaskViewCompletedBy",
    "TaskViewAssignees",
    "TaskViewCreatedBy",
    "TaskViewLastUpdatedBy",
    "TaskViewActivityLog",
    "TaskCompletedBy",
    "TaskCreatedBy",
    "TaskLastUpdatedBy",
    "TaskViewAssigneesSelectedLabour",
    "TaskViewAssigneesSelectedEmployee",
]


class Task(Dto):
    """The task body."""

    MEASURED_FROM = ("GET /api/{api_version}/tasks",)

    # Null in every record measured, so untyped.
    actual_hours: Any = None
    code: str | None = None
    completed_at: str | None = None
    completed_by: TaskCompletedBy | None = None
    created_by: TaskCreatedBy | None = None
    created_on: str | None = None
    custom_attributes: list[Any] | None = None
    description: str | None = None
    display_name: str | None = None
    due_date: str | None = None
    estimated_hours: int | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: TaskLastUpdatedBy | None = None
    last_updated_on: str | None = None
    # Null in every record measured, so untyped.
    milestone: Any = None
    name: str | None = None
    object: str | None = None
    # Null in every record measured, so untyped.
    parent_task: Any = None
    priority: str | None = None
    # Null in every record measured, so untyped.
    resource: Any = None
    sort_order: int | None = None
    # Null in every record measured, so untyped.
    start_after: Any = None
    start_date: str | None = None
    # Null in every record measured, so untyped.
    state: Any = None
    status: str | None = None
    task_status: str | None = None
    version: int | None = None
    # Null in every record measured, so untyped.
    workflow: Any = None


class TaskList(Dto):
    """One page of ``Task`` records, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/tasks",)

    data: list[Task] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class TaskView(Dto):
    """What ``get_task`` answers, under ``work_task``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/tasks/{task_id}",
        "GET /api/{api_version}/tasks/{task_id}/checklist",
        "GET /api/{api_version}/tasks/{task_id}/checklist/{task_checklist_uuid}",
        "PATCH /api/{api_version}/tasks/{task_id}",
        "POST /api/{api_version}/tasks/{task_id}/checklist",
        "POST /api/{api_version}/tasks",
        "PATCH /api/{api_version}/tasks/{task_id}/checklist/{task_checklist_uuid}",
    )

    ENVELOPE_KEY = "work_task"

    activity_logs: list[TaskViewActivityLog] | None = None
    # Null in every record measured, so untyped.
    actual_hours: Any = None
    alerts: list[Any] | None = None
    assignees: TaskViewAssignees | None = None
    checklist: Any = None
    code: str | None = None
    completed_at: str | None = None
    completed_by: TaskViewCompletedBy | None = None
    created_by: TaskViewCreatedBy | None = None
    created_on: str | None = None
    custom_attributes: list[Any] | None = None
    description: str | None = None
    display_name: str | None = None
    due_date: str | None = None
    estimated_hours: int | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: TaskViewLastUpdatedBy | None = None
    last_updated_on: str | None = None
    # Null in every record measured, so untyped.
    milestone: Any = None
    name: str | None = None
    object: str | None = None
    # Null in every record measured, so untyped.
    parent_task: Any = None
    priority: str | None = None
    # Null in every record measured, so untyped.
    resource: Any = None
    sort_order: int | None = None
    # Null in every record measured, so untyped.
    start_after: Any = None
    start_date: str | None = None
    # Null in every record measured, so untyped.
    state: Any = None
    status: str | None = None
    task_status: str | None = None
    version: int | None = None
    # Null in every record measured, so untyped.
    workflow: Any = None


class TaskNoteList(Dto):
    """One page of what ``get_task_notes`` lists, under ``data``."""

    MEASURED_FROM = ("GET /api/{api_version}/tasks/{task_code}/notes",)

    data: list[Any] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class TaskViewCompletedBy(Dto):
    """A :class:`TaskView`'s ``completed_by``."""

    name: str | None = None
    object: str | None = None


class TaskViewAssignees(Dto):
    """A :class:`TaskView`'s ``assignees``."""

    manually_added_account_contacts: list[Any] | None = None
    selected_account_contacts: list[Any] | None = None
    selected_employees: list[TaskViewAssigneesSelectedEmployee] | None = None
    selected_labours: list[TaskViewAssigneesSelectedLabour] | None = None
    selected_operators: list[Any] | None = None


class TaskViewCreatedBy(Dto):
    """A :class:`TaskView`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class TaskViewLastUpdatedBy(Dto):
    """A :class:`TaskView`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class TaskViewActivityLog(Dto):
    """One entry of a :class:`TaskView`'s ``activity_logs``."""

    activity: str | None = None


class TaskCompletedBy(Dto):
    """A :class:`Task`'s ``completed_by``."""

    name: str | None = None
    object: str | None = None


class TaskCreatedBy(Dto):
    """A :class:`Task`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class TaskLastUpdatedBy(Dto):
    """A :class:`Task`'s ``last_updated_by``."""

    name: str | None = None
    object: str | None = None


class TaskViewAssigneesSelectedLabour(Dto):
    """One entry of a :class:`TaskViewAssignees`'s ``selected_labours``."""

    display_order: int | None = None
    email: str | None = None
    labour_code: str | None = None
    name: str | None = None
    # Null in every record measured, so untyped.
    responsibility: Any = None
    uuid: str | None = None


class TaskViewAssigneesSelectedEmployee(Dto):
    """One entry of a :class:`TaskViewAssignees`'s ``selected_employees``."""

    display_order: int | None = None
    email: str | None = None
    employee_code: str | None = None
    name: str | None = None
    # Null in every record measured, so untyped.
    responsibility: Any = None
    uuid: str | None = None
