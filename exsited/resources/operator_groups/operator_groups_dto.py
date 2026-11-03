"""Typed views over the operator group bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "SettingsOperatorGroup",
    "SettingsOperatorGroupDepartment",
    "SettingsOperatorGroupList",
    "SettingsOperatorGroupRole",
]


class SettingsOperatorGroupRole(Dto):
    """A :class:`SettingsOperatorGroup`'s ``role``. A read names it as a ``role`` with its
    ``rol_`` id and ``href``; the update answer names it as a ``reference`` with the dashed uuid
    and no ``href``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class SettingsOperatorGroupDepartment(Dto):
    """One of a :class:`SettingsOperatorGroup`'s ``departments``, a ``reference``; ``id`` is null
    on the departments the instance ships with."""

    id: str | None = None
    name: str | None = None
    object: str | None = None


class SettingsOperatorGroup(Dto):
    """The operator group body, under ``operator_group``. The create answer carries only
    ``object``, ``id``, ``name``, ``display_name``, ``description`` and ``href``.
    ``created_by`` and ``last_updated_by`` are untyped."""


    ENVELOPE_KEY = "operator_group"

    created_by: Any = None
    created_on: str | None = None
    departments: list[SettingsOperatorGroupDepartment] | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    role: SettingsOperatorGroupRole | None = None
    status: str | None = None


class SettingsOperatorGroupList(Dto):
    """One page of ``SettingsOperatorGroup`` records, under ``data``."""


    data: list[SettingsOperatorGroup] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None
