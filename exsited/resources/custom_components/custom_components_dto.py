"""Typed views over the custom component bodies."""

from __future__ import annotations

from typing import Any

from exsited.dto import Dto
from exsited.resources.common.pagination_dto import Pagination

__all__ = [
    "Component",
    "ComponentList",
    "ComponentByUuid",
    "ComponentObject",
    "ComponentObjects",
    "ComponentObjectActivity",
    "ComponentObjectCustomObjects",
    "ComponentCustomForm",
    "ComponentObjectsData",
    "ComponentObjectCustomComponentObject",
    "ComponentCustomFormData",
    "ComponentObjectsDataDetail",
    "ComponentObjectsDataCustomForm",
    "ComponentObjectsDataParent",
    "ComponentObjectCustomComponentObjectDetail",
    "ComponentObjectCustomComponentObjectCustomForm",
    "ComponentObjectCustomComponentObjectParent",
    "ComponentCustomFormDataFirstColumnAttribute",
    "ComponentCustomFormDataSecondColumnAttribute",
    "ComponentCustomFormDataFirstColumnAttributeOption",
    "ComponentCustomFormDataSecondColumnAttributeTypeActual",
    "ComponentObjectRecord",
    "ComponentObjectRecordActivityLog",
    "ComponentObjectActivityEntry",
    "ComponentObjectNote",
    "ComponentObjectNotes",
    "ComponentObjectNoteAttachment",
    "ComponentObjectNoteCreatedBy",
    "ComponentObjectNoteCustomComponentObject",
    "ComponentObjectNoteLastUpdatedBy",
    "ComponentObjectNoteFiles",
    "ComponentObjectNoteFile",
]


class Component(Dto):
    """The component body, under ``component``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/component",
        "GET /api/{api_version}/component/{component_uuid}",
        "POST /api/{api_version}/component",
        "PATCH /api/{api_version}/component/{component_uuid}",
    )

    ENVELOPE_KEY = "component"

    child_custom_components: list[Any] | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    # Null in every record measured, so untyped.
    custom_component: Any = None
    custom_forms: list[ComponentCustomForm] | None = None
    custom_objects: list[Any] | None = None
    description: str | None = None
    display_name: str | None = None
    href: str | None = None
    id: str | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    last_updated_on: str | None = None
    name: str | None = None
    object: str | None = None
    relation: str | None = None
    status: str | None = None
    use_in: str | None = None
    version: int | None = None
    #: On the create answer only, and empty in every one measured.
    activity_logs: list[Any] | None = None


class ComponentList(Dto):
    """One page of ``Component`` records, under ``data``; paged by offset."""

    MEASURED_FROM = ("GET /api/{api_version}/component",)

    data: list[Component] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class ComponentByUuid(Dto):
    """The component instance body, under the component's own name, which the write functions
    unwrap; measured from the v4 collection, not the instance, so read ``.map`` when a field is
    unexpectedly None."""

    MEASURED_FROM = (
        "POST /api/{api_version}/component/{component_uuid}",
        "PATCH /api/{api_version}/component/{component_uuid}/{component_object_id}",
    )

    activity_logs: list[Any] | None = None
    attribute_groups: list[Any] | None = None
    attributes: list[Any] | None = None
    created_by: str | None = None
    created_on: str | None = None
    custom_form: dict[str, Any] | None = None
    custom_objects: list[Any] | None = None
    id: str | None = None
    last_updated_by: str | None = None
    last_updated_on: str | None = None
    parents: list[Any] | None = None
    restrictions: list[Any] | None = None
    status: str | None = None
    uuid: str | None = None
    version: str | None = None


class ComponentObject(Dto):
    """The component object body, under ``Acc Cus Comp``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/components/{component_uuid}/objects/{component_object_id}",
    )

    ENVELOPE_KEY = "Acc Cus Comp"

    attribute_groups: list[Any] | None = None
    attributes: list[Any] | None = None
    created_by: str | None = None
    created_on: str | None = None
    custom_component_object: ComponentObjectCustomComponentObject | None = None
    custom_form: dict[str, Any] | None = None
    custom_objects: list[Any] | None = None
    id: str | None = None
    last_updated_by: str | None = None
    last_updated_on: str | None = None
    parents: list[Any] | None = None
    restrictions: list[Any] | None = None
    status: str | None = None
    uuid: str | None = None
    version: str | None = None


class ComponentObjects(Dto):
    """The component objects body."""

    MEASURED_FROM = ("GET /api/{api_version}/components/{component_uuid}/objects",)

    data: list[ComponentObjectsData] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class ComponentObjectActivity(Dto):
    """The component object activity body, under ``Acc Cus Comp``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/components/{component_uuid}/objects/{component_object_id}/activity",
    )

    ENVELOPE_KEY = "Acc Cus Comp"

    activites: list[Any] | None = None
    data: list[Any] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class ComponentObjectCustomObjects(Dto):
    """The component object custom objects body."""

    MEASURED_FROM = (
        "GET /api/{api_version}/components/{component_uuid}/objects/{component_object_id}/custom_objects",
    )

    custom_objects: list[Any] | None = None
    data: list[Any] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class ComponentCustomForm(Dto):
    """One entry of a :class:`Component`'s ``custom_forms``."""

    column_count: int | None = None
    data: ComponentCustomFormData | None = None
    id: str | None = None
    object: str | None = None
    template_name: str | None = None


class ComponentObjectsData(Dto):
    """One entry of a :class:`ComponentObjects`'s ``data``."""

    accounts: list[Any] | None = None
    attribute_groups: list[Any] | None = None
    attributes: list[Any] | None = None
    code: str | None = None
    component: ComponentObjectsDataDetail | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    custom_form: ComponentObjectsDataCustomForm | None = None
    custom_objects: list[Any] | None = None
    href: str | None = None
    id: str | None = None
    items: list[Any] | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    object: str | None = None
    orders: list[Any] | None = None
    parents: list[ComponentObjectsDataParent] | None = None
    quotes: list[Any] | None = None
    restrictions: list[Any] | None = None
    status: str | None = None
    version: int | None = None
    workflow_data: list[Any] | None = None
    # Null in every record measured, so untyped.
    workflow_stage: Any = None
    # Null in every record measured, so untyped.
    workflow_status: Any = None
    # Null in every record measured, so untyped.
    workflow_status_uuid: Any = None


class ComponentObjectCustomComponentObject(Dto):
    """A :class:`ComponentObject`'s ``custom_component_object``."""

    accounts: list[Any] | None = None
    attribute_groups: list[Any] | None = None
    attributes: list[Any] | None = None
    code: str | None = None
    component: ComponentObjectCustomComponentObjectDetail | None = None
    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    custom_form: ComponentObjectCustomComponentObjectCustomForm | None = None
    custom_objects: list[Any] | None = None
    href: str | None = None
    id: str | None = None
    items: list[Any] | None = None
    # Null in every record measured, so untyped.
    last_updated_by: Any = None
    # Null in every record measured, so untyped.
    last_updated_on: Any = None
    object: str | None = None
    orders: list[Any] | None = None
    parents: list[ComponentObjectCustomComponentObjectParent] | None = None
    quotes: list[Any] | None = None
    restrictions: list[Any] | None = None
    status: str | None = None
    version: int | None = None
    workflow_data: list[Any] | None = None
    # Null in every record measured, so untyped.
    workflow_stage: Any = None
    # Null in every record measured, so untyped.
    workflow_status: Any = None
    # Null in every record measured, so untyped.
    workflow_status_uuid: Any = None


class ComponentCustomFormData(Dto):
    """A :class:`ComponentCustomForm`'s ``data``."""

    firstColumnAttribute: list[ComponentCustomFormDataFirstColumnAttribute] | None = None
    secondColumnAttribute: list[ComponentCustomFormDataSecondColumnAttribute] | None = None
    thirdColumnAttribute: list[Any] | None = None


class ComponentObjectsDataDetail(Dto):
    """A :class:`ComponentObjectsData`'s ``component``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ComponentObjectsDataCustomForm(Dto):
    """A :class:`ComponentObjectsData`'s ``custom_form``."""

    id: str | None = None
    name: str | None = None
    object: str | None = None


class ComponentObjectsDataParent(Dto):
    """One entry of a :class:`ComponentObjectsData`'s ``parents``."""

    email: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    type: str | None = None


class ComponentObjectCustomComponentObjectDetail(Dto):
    """A :class:`ComponentObjectCustomComponentObject`'s ``component``."""

    href: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None


class ComponentObjectCustomComponentObjectCustomForm(Dto):
    """A :class:`ComponentObjectCustomComponentObject`'s ``custom_form``."""

    id: str | None = None
    name: str | None = None
    object: str | None = None


class ComponentObjectCustomComponentObjectParent(Dto):
    """One entry of a :class:`ComponentObjectCustomComponentObject`'s ``parents``."""

    email: str | None = None
    id: str | None = None
    name: str | None = None
    object: str | None = None
    type: str | None = None


class ComponentCustomFormDataFirstColumnAttribute(Dto):
    """One entry of a :class:`ComponentCustomFormData`'s ``firstColumnAttribute``."""

    canEncrypt: bool | None = None
    description: str | None = None
    displayName: str | None = None
    enabled: bool | None = None
    encryptData: bool | None = None
    # Null in every record measured, so untyped.
    entity: Any = None
    fieldRequired: bool | None = None
    formMaxLengthInputed: bool | None = None
    formMinLengthInputed: bool | None = None
    id: int | None = None
    ids: int | None = None
    isRequired: bool | None = None
    isUnique: bool | None = None
    # Null in every record measured, so untyped.
    maxLength: Any = None
    metaData: str | None = None
    # Null in every record measured, so untyped.
    minLength: Any = None
    name: str | None = None
    options: list[ComponentCustomFormDataFirstColumnAttributeOption] | None = None
    position: str | None = None
    showInListView: bool | None = None
    # Null in every record measured, so untyped.
    timeFormat: Any = None
    type: str | None = None
    typeValue: str | None = None
    validationMessage: str | None = None
    validationMessageRequired: bool | None = None
    value: str | None = None


class ComponentCustomFormDataSecondColumnAttribute(Dto):
    """One entry of a :class:`ComponentCustomFormData`'s ``secondColumnAttribute``."""

    displayName: str | None = None
    fieldEnabled: bool | None = None
    fieldRequired: bool | None = None
    ids: int | None = None
    name: str | None = None
    showInListView: bool | None = None
    type: str | None = None
    typeActual: ComponentCustomFormDataSecondColumnAttributeTypeActual | None = None
    validationMessageRequired: bool | None = None


class ComponentCustomFormDataFirstColumnAttributeOption(Dto):
    """One entry of a :class:`ComponentCustomFormDataFirstColumnAttribute`'s ``options``."""

    id: str | None = None
    name: str | None = None


class ComponentCustomFormDataSecondColumnAttributeTypeActual(Dto):
    """A :class:`ComponentCustomFormDataSecondColumnAttribute`'s ``typeActual``."""

    key: str | None = None
    value: str | None = None


class ComponentObjectRecord(ComponentObjectCustomComponentObject):
    """The component object body a v4 write answers, under ``custom_component_object``: the
    fields a read nests there, with ``activity_logs`` beside them."""

    MEASURED_FROM = (
        "POST /api/{api_version}/components/{component_uuid}/objects",
        "PATCH /api/{api_version}/components/{component_uuid}/objects/{component_object_id}",
    )

    ENVELOPE_KEY = "custom_component_object"

    activity_logs: list[ComponentObjectRecordActivityLog] | None = None
    last_updated_on: str | None = None


class ComponentObjectRecordActivityLog(Dto):
    """One entry of a :class:`ComponentObjectRecord`'s ``activity_logs``."""

    activity: str | None = None


class ComponentObjectActivityEntry(Dto):
    """One component object activity, under ``custom_component_object_activity``."""

    MEASURED_FROM = (
        "POST /api/{api_version}/components/{component_uuid}/objects/{component_object_id}"
        "/activity",
        "GET /api/{api_version}/components/{component_uuid}/objects/{component_object_id}"
        "/activity/{activity_id}",
    )

    ENVELOPE_KEY = "custom_component_object_activity"

    # Null in every record measured, so untyped.
    created_by: Any = None
    created_on: str | None = None
    href: str | None = None
    id: str | None = None
    message: str | None = None
    object: str | None = None
    status: str | None = None
    type: str | None = None
    user_name: str | None = None
    version: int | None = None


class ComponentObjectNote(Dto):
    """A component object's note, under ``note``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/components/{component_uuid}/objects/{component_object_id}/notes",
        "GET /api/{api_version}/components/{component_uuid}/objects/{component_object_id}"
        "/notes/{note_id}",
        "POST /api/{api_version}/components/{component_uuid}/objects/{component_object_id}/notes",
        "PATCH /api/{api_version}/components/{component_uuid}/objects/{component_object_id}"
        "/notes/{note_id}",
    )

    ENVELOPE_KEY = "note"

    attachments: list[ComponentObjectNoteAttachment] | None = None
    content: str | None = None
    created_by: ComponentObjectNoteCreatedBy | None = None
    created_on: str | None = None
    custom_component_object: ComponentObjectNoteCustomComponentObject | None = None
    # Null in every record measured, so untyped.
    group: Any = None
    href: str | None = None
    id: str | None = None
    last_updated_by: ComponentObjectNoteLastUpdatedBy | None = None
    last_updated_on: str | None = None
    object: str | None = None
    # Null in every record measured, so untyped.
    user: Any = None
    version: int | None = None
    watchers: list[Any] | None = None


class ComponentObjectNotes(Dto):
    """One page of ``ComponentObjectNote`` records, under ``data``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/components/{component_uuid}/objects/{component_object_id}/notes",
    )

    data: list[ComponentObjectNote] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class ComponentObjectNoteAttachment(Dto):
    """One entry of a :class:`ComponentObjectNote`'s ``attachments``; ``uuid`` is the file id."""

    content_type: str | None = None
    filename: str | None = None
    href: str | None = None
    size: int | None = None
    uuid: str | None = None


class ComponentObjectNoteCreatedBy(Dto):
    """A :class:`ComponentObjectNote`'s ``created_by``."""

    name: str | None = None
    object: str | None = None


class ComponentObjectNoteCustomComponentObject(Dto):
    """A :class:`ComponentObjectNote`'s ``custom_component_object``, the note's owner."""

    href: str | None = None
    id: str | None = None
    object: str | None = None


class ComponentObjectNoteLastUpdatedBy(Dto):
    """A :class:`ComponentObjectNote`'s ``last_updated_by``, set once the note has been updated."""

    name: str | None = None
    object: str | None = None


class ComponentObjectNoteFiles(Dto):
    """A note's files, under ``data``; its ``pagination`` carries ``has_more`` alone."""

    MEASURED_FROM = (
        "GET /api/{api_version}/components/{component_uuid}/objects/{component_object_id}"
        "/notes/{note_id}/files",
    )

    data: list[ComponentObjectNoteAttachment] | None = None
    object: str | None = None
    pagination: Pagination | None = None
    url: str | None = None


class ComponentObjectNoteFile(ComponentObjectNoteAttachment):
    """One file of a note, under ``file``."""

    MEASURED_FROM = (
        "GET /api/{api_version}/components/{component_uuid}/objects/{component_object_id}"
        "/notes/{note_id}/files/{file_id}",
    )

    ENVELOPE_KEY = "file"
