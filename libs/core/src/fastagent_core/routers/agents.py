"""Agents router."""

from fastapi import APIRouter, status

router = APIRouter(prefix="/v1", tags=["agents"])


async def invoke_agent_handler() -> dict[str, str]:
    """Invoke an agent."""
    return {"message": "not implemented"}


async def batch_agents_handler() -> dict[str, str]:
    """Batch multiple inference requests to an agent."""
    return {"message": "not implemented"}


router.add_api_route(
    "/agents/invoke",
    invoke_agent_handler,
    methods=["POST"],
    status_code=status.HTTP_200_OK,
)
router.add_api_route(
    "/agents/batch",
    batch_agents_handler,
    methods=["POST"],
    status_code=status.HTTP_200_OK,
)
