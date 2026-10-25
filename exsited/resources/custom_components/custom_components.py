"""Custom component endpoints, under ``/api/{api_version}``."""

from __future__ import annotations

from functools import lru_cache
from typing import Any, Mapping, Sequence

from exsited.client.api_response import ApiResponse
from exsited.dto import Dto
from exsited.errors import SdkUsageError
from exsited.resources.custom_components import custom_components_urls
from exsited.resources.custom_components.custom_components_dto import (
    Component,
    ComponentByUuid,
    ComponentList,
    ComponentObject,
    ComponentObjectActivity,
    ComponentObjectActivityEntry,
    ComponentObjectCustomObjects,
    ComponentObjectNote,
    ComponentObjectNoteFile,
    ComponentObjectNoteFiles,
    ComponentObjectNotes,
    ComponentObjectRecord,
    ComponentObjects,
)

__all__ = [
    "get_component",
    "get_component_by_uuid",
    "create_component_by_uuid",
    "delete_component_by_id",
    "update_component_by_id",
    "get_component_objects",
    "get_component_object",
    "get_component_object_activity",
    "get_component_object_custom_objects",
    "get_component_object_pdf",
    "create_component",
    "update_component",
    "delete_component",
    "create_component_object",
    "update_component_object",
    "delete_component_object",
    "create_component_object_activity",
    "get_component_object_activity_by_id",
    "get_component_object_milestones",
    "get_component_object_milestone",
    "get_component_object_history",
    "get_component_object_history_by_id",
    "get_component_object_notes",
    "get_component_object_note",
    "get_component_object_note_files",
    "get_component_object_note_file",
    "create_component_object_note",
    "update_component_object_note",
    "delete_component_object_note",
    "delete_component_object_note_file",
    "get_component_object_custom_object",
    "create_component_object_custom_object_instance",
    "get_component_object_custom_object_instance",
    "update_component_object_custom_object_instance",
    "delete_component_object_custom_object_instance",
    "link_component_object_domains",
    "update_component_object_domains",
    "unlink_component_object_domains",
    "change_component_object_status",
]

#: The key a listing puts its records under.
RECORD_KEY = "data"

CustomComponentPayload = Mapping[str, Any] | str | Dto


def get_component(
    client: Any,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentList]:
    """List all component definitions - ``GET /component``."""
    return client.send_get_request(
        custom_components_urls.COMPONENT,
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentList,
    )


def get_component_by_uuid(
    client: Any,
    component_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Component]:
    """Single component definition - ``GET /component/{component_uuid}``."""
    return client.send_get_request(
        custom_components_urls.COMPONENT_BY_UUID,
        path_params={"component_uuid": component_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Component,
    )


def create_component_by_uuid(
    client: Any,
    component_uuid: str,
    payload: CustomComponentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentByUuid]:
    """Create new instance - ``POST /component/{component_uuid}``; answered ``201`` under
    the component's name."""
    _require_payload(payload)
    return client.send_post_request(
        custom_components_urls.COMPONENT_BY_UUID,
        path_params={"component_uuid": component_uuid},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=_instance_view(payload),
    )


def delete_component_by_id(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete instance - ``DELETE /component/{component_uuid}/{component_object_id}``;
    answered ``204``."""
    return client.send_delete_request(
        custom_components_urls.COMPONENT_BY_ID,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_component_by_id(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    payload: CustomComponentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentByUuid]:
    """Update instance - ``PATCH /component/{component_uuid}/{component_object_id}``;
    answered ``202``."""
    _require_payload(payload)
    return client.send_patch_request(
        custom_components_urls.COMPONENT_BY_ID,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=_instance_view(payload),
    )


def get_component_objects(
    client: Any,
    component_uuid: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjects]:
    """List all instances - ``GET /components/{component_uuid}/objects``."""
    return client.send_get_request(
        custom_components_urls.COMPONENT_OBJECTS,
        path_params={"component_uuid": component_uuid},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjects,
    )


def get_component_object(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObject]:
    """Single instance - ``GET /components/{component_uuid}/objects/{component_object_id}``."""
    return client.send_get_request(
        custom_components_urls.COMPONENT_OBJECT,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObject,
    )


def get_component_object_activity(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjectActivity]:
    """Activity log -
    ``GET /components/{component_uuid}/objects/{component_object_id}/activity``."""
    return client.send_get_request(
        custom_components_urls.COMPONENT_OBJECT_ACTIVITY,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjectActivity,
    )


def get_component_object_custom_objects(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjectCustomObjects]:
    """List linked custom objects -
    ``GET /components/{component_uuid}/objects/{component_object_id}/custom_objects``."""
    return client.send_get_request(
        custom_components_urls.COMPONENT_OBJECT_CUSTOM_OBJECTS,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjectCustomObjects,
    )


def get_component_object_pdf(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """PDF descriptor - ``GET /components/{component_uuid}/objects/{component_object_id}/pdf``."""
    return client.send_get_request(
        custom_components_urls.COMPONENT_OBJECT_PDF,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_component(
    client: Any,
    payload: CustomComponentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Component]:
    """Create a component definition - ``POST /component``, under ``component``; ``name`` is
    required, and ``use_in`` asks for ``relation`` beside it."""
    _require_payload(payload)
    return client.send_post_request(
        custom_components_urls.COMPONENT,
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Component,
    )


def update_component(
    client: Any,
    component_uuid: str,
    payload: CustomComponentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[Component]:
    """Update a component definition - ``PATCH /component/{component_uuid}``, the ``cmp_`` id,
    under ``component``."""
    _require_payload(payload)
    return client.send_patch_request(
        custom_components_urls.COMPONENT_BY_UUID,
        path_params={"component_uuid": component_uuid},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=Component,
    )


def delete_component(
    client: Any,
    component_uuid: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a component definition - ``DELETE /component/{component_uuid}``, the ``cmp_`` id;
    answered ``204``, and ``404`` once it is gone."""
    return client.send_delete_request(
        custom_components_urls.COMPONENT_BY_UUID,
        path_params={"component_uuid": component_uuid},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_component_object(
    client: Any,
    component_uuid: str,
    payload: CustomComponentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjectRecord]:
    """Create an instance on v4 - ``POST /components/{component_uuid}/objects``, under
    ``custom_component_object``; every key is optional, and ``parents`` names the owner."""
    _require_payload(payload)
    return client.send_post_request(
        custom_components_urls.COMPONENT_OBJECTS,
        path_params={"component_uuid": component_uuid},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjectRecord,
    )


def update_component_object(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    payload: CustomComponentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjectRecord]:
    """Update an instance on v4 -
    ``PATCH /components/{component_uuid}/objects/{component_object_id}``; ``version_id`` must
    match when sent, and ``code``, ``parents`` and ``custom_form`` are refused."""
    _require_payload(payload)
    return client.send_patch_request(
        custom_components_urls.COMPONENT_OBJECT,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjectRecord,
    )


def delete_component_object(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete an instance on v4 -
    ``DELETE /components/{component_uuid}/objects/{component_object_id}``; answered ``204``."""
    return client.send_delete_request(
        custom_components_urls.COMPONENT_OBJECT,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_component_object_activity(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    payload: CustomComponentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjectActivityEntry]:
    """Log an activity -
    ``POST /components/{component_uuid}/objects/{component_object_id}/activity``, under
    ``custom_component_object_activity`` with ``type``, ``message`` and ``user_name``."""
    _require_payload(payload)
    return client.send_post_request(
        custom_components_urls.COMPONENT_OBJECT_ACTIVITY,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjectActivityEntry,
    )


def get_component_object_activity_by_id(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    activity_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjectActivityEntry]:
    """One activity -
    ``GET /components/{component_uuid}/objects/{component_object_id}/activity/{activity_id}``."""
    return client.send_get_request(
        custom_components_urls.COMPONENT_OBJECT_ACTIVITY_ENTRY,
        path_params={
            "component_uuid": component_uuid,
            "component_object_id": component_object_id,
            "activity_id": activity_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjectActivityEntry,
    )


def get_component_object_milestones(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """List workflow milestones -
    ``GET /components/{component_uuid}/objects/{component_object_id}/milestones``; every listing
    measured was empty, so ``.dto`` is None."""
    return client.send_get_request(
        custom_components_urls.COMPONENT_OBJECT_MILESTONES,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_component_object_milestone(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    milestone_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """One workflow milestone -
    ``GET /components/{component_uuid}/objects/{component_object_id}/milestones/{milestone_id}``,
    the ``wfm_`` id."""
    return client.send_get_request(
        custom_components_urls.COMPONENT_OBJECT_MILESTONE,
        path_params={
            "component_uuid": component_uuid,
            "component_object_id": component_object_id,
            "milestone_id": milestone_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_component_object_history(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """List workflow history -
    ``GET /components/{component_uuid}/objects/{component_object_id}/history``; every listing
    measured was empty, so ``.dto`` is None."""
    return client.send_get_request(
        custom_components_urls.COMPONENT_OBJECT_HISTORY,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_component_object_history_by_id(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    history_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """One workflow history entry -
    ``GET /components/{component_uuid}/objects/{component_object_id}/history/{history_id}``, the
    ``wfh_`` id."""
    return client.send_get_request(
        custom_components_urls.COMPONENT_OBJECT_HISTORY_ENTRY,
        path_params={
            "component_uuid": component_uuid,
            "component_object_id": component_object_id,
            "history_id": history_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_component_object_notes(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    query_params: Mapping[str, Any] | None = None,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjectNotes]:
    """List notes - ``GET /components/{component_uuid}/objects/{component_object_id}/notes``."""
    return client.send_get_request(
        custom_components_urls.COMPONENT_OBJECT_NOTES,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        query_params=query_params,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjectNotes,
    )


def get_component_object_note(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjectNote]:
    """One note -
    ``GET /components/{component_uuid}/objects/{component_object_id}/notes/{note_id}``."""
    return client.send_get_request(
        custom_components_urls.COMPONENT_OBJECT_NOTE,
        path_params={
            "component_uuid": component_uuid,
            "component_object_id": component_object_id,
            "note_id": note_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjectNote,
    )


def get_component_object_note_files(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjectNoteFiles]:
    """List a note's files -
    ``GET /components/{component_uuid}/objects/{component_object_id}/notes/{note_id}/files``."""
    return client.send_get_request(
        custom_components_urls.COMPONENT_OBJECT_NOTE_FILES,
        path_params={
            "component_uuid": component_uuid,
            "component_object_id": component_object_id,
            "note_id": note_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjectNoteFiles,
    )


def get_component_object_note_file(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjectNoteFile]:
    """One file of a note - ``GET /components/{component_uuid}/objects/{component_object_id}``
    ``/notes/{note_id}/files/{file_id}``, the attachment's ``uuid``."""
    return client.send_get_request(
        custom_components_urls.COMPONENT_OBJECT_NOTE_FILE,
        path_params={
            "component_uuid": component_uuid,
            "component_object_id": component_object_id,
            "note_id": note_id,
            "file_id": file_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjectNoteFile,
    )


def create_component_object_note(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    note: str,
    *,
    files: Mapping[str, Any] | Sequence[tuple[str, Any]] | None = None,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjectNote]:
    """Attach a note - ``POST /components/{component_uuid}/objects/{component_object_id}/notes``;
    a form, the text as the ``note`` field with any ``files`` beside it."""
    _require_note(note)
    return client.send_post_request(
        custom_components_urls.COMPONENT_OBJECT_NOTES,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjectNote,
    )


def update_component_object_note(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    note_id: str,
    note: str,
    *,
    files: Mapping[str, Any] | Sequence[tuple[str, Any]] | None = None,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjectNote]:
    """Update a note -
    ``PATCH /components/{component_uuid}/objects/{component_object_id}/notes/{note_id}``; a form,
    as the create is."""
    _require_note(note)
    return client.send_patch_request(
        custom_components_urls.COMPONENT_OBJECT_NOTE,
        path_params={
            "component_uuid": component_uuid,
            "component_object_id": component_object_id,
            "note_id": note_id,
        },
        form_data={"note": note},
        files=files,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjectNote,
    )


def delete_component_object_note(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    note_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a note -
    ``DELETE /components/{component_uuid}/objects/{component_object_id}/notes/{note_id}``;
    answered ``204``."""
    return client.send_delete_request(
        custom_components_urls.COMPONENT_OBJECT_NOTE,
        path_params={
            "component_uuid": component_uuid,
            "component_object_id": component_object_id,
            "note_id": note_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_component_object_note_file(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    note_id: str,
    file_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a note's file - ``DELETE /components/{component_uuid}/objects/{component_object_id}``
    ``/notes/{note_id}/files/{file_id}``, the attachment's ``uuid``; answered ``204``."""
    return client.send_delete_request(
        custom_components_urls.COMPONENT_OBJECT_NOTE_FILE,
        path_params={
            "component_uuid": component_uuid,
            "component_object_id": component_object_id,
            "note_id": note_id,
            "file_id": file_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_component_object_custom_object(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    custom_object_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """One custom object schema with its instances - ``GET /components/{component_uuid}/objects``
    ``/{component_object_id}/custom_objects/{custom_object_id}``."""
    return client.send_get_request(
        custom_components_urls.COMPONENT_OBJECT_CUSTOM_OBJECT,
        path_params={
            "component_uuid": component_uuid,
            "component_object_id": component_object_id,
            "custom_object_id": custom_object_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def create_component_object_custom_object_instance(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    custom_object_id: str,
    payload: CustomComponentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Create a custom object instance - ``POST /components/{component_uuid}/objects``
    ``/{component_object_id}/custom_objects/{custom_object_id}``, under ``custom_object_instances``
    with an ``attributes`` list; the path has no ``instances`` segment."""
    _require_payload(payload)
    return client.send_post_request(
        custom_components_urls.COMPONENT_OBJECT_CUSTOM_OBJECT,
        path_params={
            "component_uuid": component_uuid,
            "component_object_id": component_object_id,
            "custom_object_id": custom_object_id,
        },
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def get_component_object_custom_object_instance(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    custom_object_id: str,
    instance_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """One custom object instance - ``GET /components/{component_uuid}/objects``
    ``/{component_object_id}/custom_objects/{custom_object_id}/instances/{instance_id}``."""
    return client.send_get_request(
        custom_components_urls.COMPONENT_OBJECT_CUSTOM_OBJECT_INSTANCE,
        path_params={
            "component_uuid": component_uuid,
            "component_object_id": component_object_id,
            "custom_object_id": custom_object_id,
            "instance_id": instance_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def update_component_object_custom_object_instance(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    custom_object_id: str,
    instance_id: str,
    payload: CustomComponentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Update a custom object instance - ``PATCH /components/{component_uuid}/objects``
    ``/{component_object_id}/custom_objects/{custom_object_id}/instances/{instance_id}``, under
    ``custom_object_instance`` with an ``attributes`` list."""
    _require_payload(payload)
    return client.send_patch_request(
        custom_components_urls.COMPONENT_OBJECT_CUSTOM_OBJECT_INSTANCE,
        path_params={
            "component_uuid": component_uuid,
            "component_object_id": component_object_id,
            "custom_object_id": custom_object_id,
            "instance_id": instance_id,
        },
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def delete_component_object_custom_object_instance(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    custom_object_id: str,
    instance_id: str,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse:
    """Delete a custom object instance - ``DELETE /components/{component_uuid}/objects``
    ``/{component_object_id}/custom_objects/{custom_object_id}/instances/{instance_id}``."""
    return client.send_delete_request(
        custom_components_urls.COMPONENT_OBJECT_CUSTOM_OBJECT_INSTANCE,
        path_params={
            "component_uuid": component_uuid,
            "component_object_id": component_object_id,
            "custom_object_id": custom_object_id,
            "instance_id": instance_id,
        },
        raise_on_error=raise_on_error,
        response_format=response_format,
    )


def link_component_object_domains(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    payload: CustomComponentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjectRecord]:
    """Link accounts or orders -
    ``POST /components/{component_uuid}/objects/{component_object_id}/link_domains``, under
    ``custom_component_object`` with ``domain_type`` and ``domains[].domain_id``."""
    _require_payload(payload)
    return client.send_post_request(
        custom_components_urls.COMPONENT_OBJECT_LINK_DOMAINS,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjectRecord,
    )


def update_component_object_domains(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    payload: CustomComponentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjectRecord]:
    """Replace the linked accounts or orders -
    ``PATCH /components/{component_uuid}/objects/{component_object_id}/link_domains``; a domain
    left out of ``domains`` is unlinked."""
    _require_payload(payload)
    return client.send_patch_request(
        custom_components_urls.COMPONENT_OBJECT_LINK_DOMAINS,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjectRecord,
    )


def unlink_component_object_domains(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    payload: CustomComponentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjectRecord]:
    """Unlink accounts or orders -
    ``POST /components/{component_uuid}/objects/{component_object_id}/unlink_domains``; a domain
    that is not linked is refused."""
    _require_payload(payload)
    return client.send_post_request(
        custom_components_urls.COMPONENT_OBJECT_UNLINK_DOMAINS,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjectRecord,
    )


def change_component_object_status(
    client: Any,
    component_uuid: str,
    component_object_id: str,
    payload: CustomComponentPayload,
    *,
    raise_on_error: bool | None = None,
    response_format: str | None = None,
) -> ApiResponse[ComponentObjectRecord]:
    """Move an instance through its workflow -
    ``POST /components/{component_uuid}/objects/{component_object_id}/change_status``, under
    ``custom_component_object`` with ``workflow_status``; runs the transition at once."""
    _require_payload(payload)
    return client.send_post_request(
        custom_components_urls.COMPONENT_OBJECT_CHANGE_STATUS,
        path_params={"component_uuid": component_uuid, "component_object_id": component_object_id},
        json_body=payload,
        raise_on_error=raise_on_error,
        response_format=response_format,
        dto_type=ComponentObjectRecord,
    )


def _instance_view(payload: CustomComponentPayload) -> type[ComponentByUuid]:
    """The instance view under the one key the payload names, which the answer is keyed by too."""
    body = payload.to_map() if isinstance(payload, Dto) else payload
    if isinstance(body, Mapping) and len(body) == 1:
        (name,) = body
        if isinstance(name, str):
            return _view_under(name)
    return ComponentByUuid


@lru_cache(maxsize=64)
def _view_under(name: str) -> type[ComponentByUuid]:
    return type(
        ComponentByUuid.__name__,
        (ComponentByUuid,),
        {"ENVELOPE_KEY": name, "__module__": ComponentByUuid.__module__},
    )


def _require_payload(payload: Any) -> None:
    if payload is None:
        raise SdkUsageError(
            "payload is required: this endpoint takes a body, and None would "
            "send the request with no body at all"
        )


def _require_note(note: Any) -> None:
    # A None note would go out as the text "None" and be stored as the note.
    if note is None:
        raise SdkUsageError(
            "note is required: the note text is the body of this request, and "
            "None would be encoded as the string 'None' and stored as the note"
        )
