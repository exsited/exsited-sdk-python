"""Path templates and body keys for the custom component endpoints."""

from __future__ import annotations

COMPONENT = "/api/{api_version}/component"
COMPONENT_BY_UUID = "/api/{api_version}/component/{component_uuid}"
COMPONENT_BY_ID = "/api/{api_version}/component/{component_uuid}/{component_object_id}"

COMPONENT_OBJECTS = "/api/{api_version}/components/{component_uuid}/objects"
COMPONENT_OBJECT = "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}"
COMPONENT_OBJECT_ACTIVITY = (
    "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}/activity"
)
COMPONENT_OBJECT_CUSTOM_OBJECTS = (
    "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}/custom_objects"
)
COMPONENT_OBJECT_PDF = (
    "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}/pdf"
)
COMPONENT_OBJECT_ACTIVITY_ENTRY = (
    "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}"
    "/activity/{activity_id}"
)
COMPONENT_OBJECT_MILESTONES = (
    "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}/milestones"
)
COMPONENT_OBJECT_MILESTONE = (
    "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}"
    "/milestones/{milestone_id}"
)
#: ``history`` is singular on the wire, for the list and for one entry alike.
COMPONENT_OBJECT_HISTORY = (
    "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}/history"
)
COMPONENT_OBJECT_HISTORY_ENTRY = (
    "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}"
    "/history/{history_id}"
)
COMPONENT_OBJECT_NOTES = (
    "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}/notes"
)
COMPONENT_OBJECT_NOTE = (
    "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}/notes/{note_id}"
)
COMPONENT_OBJECT_NOTE_FILES = (
    "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}"
    "/notes/{note_id}/files"
)
COMPONENT_OBJECT_NOTE_FILE = (
    "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}"
    "/notes/{note_id}/files/{file_id}"
)
#: A custom object instance is created on the schema's own path, with no ``instances``
#: segment; it is read, updated and deleted under ``instances/{instance_id}``.
COMPONENT_OBJECT_CUSTOM_OBJECT = (
    "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}"
    "/custom_objects/{custom_object_id}"
)
COMPONENT_OBJECT_CUSTOM_OBJECT_INSTANCE = (
    "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}"
    "/custom_objects/{custom_object_id}/instances/{instance_id}"
)
COMPONENT_OBJECT_LINK_DOMAINS = (
    "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}/link_domains"
)
COMPONENT_OBJECT_UNLINK_DOMAINS = (
    "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}/unlink_domains"
)
COMPONENT_OBJECT_CHANGE_STATUS = (
    "/api/{api_version}/components/{component_uuid}/objects/{component_object_id}/change_status"
)

#: The key a listing's records sit under.
COMPONENT_LISTING_KEY = "data"
COMPONENT_OBJECTS_KEY = "data"
COMPONENT_OBJECT_NOTES_KEY = "data"
COMPONENT_OBJECT_NOTE_FILES_KEY = "data"

#: The envelope one record arrives under.
ACC_CUS_COMP_KEY = "Acc Cus Comp"
COMPONENT_KEY = "component"
CUSTOM_COMPONENT_OBJECT_KEY = "custom_component_object"
CUSTOM_COMPONENT_OBJECT_ACTIVITY_KEY = "custom_component_object_activity"
NOTE_KEY = "note"
FILE_KEY = "file"

#: The body a custom object instance create sends, a plural key over one instance, and the
#: singular one the update sends and both answer under.
CUSTOM_OBJECT_INSTANCES_KEY = "custom_object_instances"
CUSTOM_OBJECT_INSTANCE_KEY = "custom_object_instance"
