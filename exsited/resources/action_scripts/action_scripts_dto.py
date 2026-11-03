"""Typed views over the action script bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "ActionScript",
    "ActionScriptList",
    "ActionScriptCreatedBy",
    "ActionScriptLastUpdatedBy",
]


class ActionScript(Dto):
    """The action script body, under ``action_script``; ``activity_logs`` comes on the create
    answer only."""


    ENVELOPE_KEY = "action_script"

    action_name: Any = None
    activity_logs: list[Any] | None = None
    created_by: ActionScriptCreatedBy | None = None
    created_on: str | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: ActionScriptLastUpdatedBy | None = None
    last_updated_on: Any = None
    name: str | None = None
    object: str | None = None
    object_name: Any = None
    status: str | None = None


class ActionScriptList(Dto):
    """One page of ``ActionScript`` records, under ``data``."""


    data: list[ActionScript] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class ActionScriptCreatedBy(Dto):
    """An :class:`ActionScript`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class ActionScriptLastUpdatedBy(Dto):
    """An :class:`ActionScript`'s ``last_updated_by``, set once the script has been updated."""

    name: str | None = None
    object: str | None = None
