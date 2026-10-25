"""Path templates and body keys for the workflow endpoints."""

from __future__ import annotations

WORKFLOWS = "/api/{api_version}/workflows"
WORKFLOW = "/api/{api_version}/workflows/{workflow_id}"
WORKFLOW_MILESTONES = "/api/{api_version}/workflows/{workflow_uuid}/milestones"
WORKFLOW_MILESTONE = "/api/{api_version}/workflows/{workflow_id}/milestones/{milestone_id}"
WORKFLOW_STAGES = "/api/{api_version}/workflows/{workflow_id}/stages"
WORKFLOW_STAGE = "/api/{api_version}/workflows/{workflow_id}/stages/{stage_id}"
MILESTONE = "/api/{api_version}/milestones/{milestone_uuid}"

# One component instance's workflow on v4. ``{component_uuid}`` is the component's dashed uuid,
# the hex of its ``cmp_`` id with the dashes put back; the ``cmp_`` id itself is a 404.
# ``{object_code}`` is the instance's ``code``, not its ``cco_`` id.
WORKFLOW_CUSTOM_COMPONENT_HISTORY = (
    "/api/{api_version}/workflows/custom_components/{component_uuid}/{object_code}/history"
)
WORKFLOW_CUSTOM_COMPONENT_MILESTONES = (
    "/api/{api_version}/workflows/custom_components/{component_uuid}/{object_code}/milestones"
)
WORKFLOW_CUSTOM_COMPONENT_MILESTONE = (
    "/api/{api_version}/workflows/custom_components/{component_uuid}/{object_code}/milestones/"
    "{milestone_id}"
)

#: ``{component_object_id}`` on the two ``/workflow/component`` reads is the instance's code.
WORKFLOW_COMPONENT_HISTORY = "/api/{api_version}/workflow/component/{component_object_id}/history"
WORKFLOW_COMPONENT_CC_INSTANCE_CC_MILESTONE = (
    "/api/{api_version}/workflow/component/{component_uuid}/{component_object_id}/milestone"
)

#: The key a listing's records sit under.
WORKFLOWS_KEY = "data"
WORKFLOW_MILESTONES_KEY = "data"
WORKFLOW_STAGES_KEY = "data"

#: The envelope one record arrives under, and the one a create or an update is sent under.
WORKFLOW_KEY = "workflow"
WORKFLOW_MILESTONE_KEY = "workflow_milestone"
WORKFLOW_STAGE_KEY = "workflow_stage"
WORKFLOW_MILESTONE_INSTANCE_KEY = "workflow_milestone_instance"
