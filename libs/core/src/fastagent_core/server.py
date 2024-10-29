"""FastAgent server."""

from typing import Literal

from fastagent_core.api import FastAgentAPI

MIN_PORT = 1024
MAX_PORT = 65535


class FastAgentServer:
    def __init__(self, api: FastAgentAPI) -> None:
        pass

    async def setup_routes(self: "FastAgentServer") -> None:
        """Setup routes."""
        pass

    async def setup_server(self: "FastAgentServer") -> None:
        """Setup the server."""
        pass

    async def setup_middlewares(self: "FastAgentServer") -> None:
        """Setup middlewares."""
        pass

    async def run(
        self: "FastAgentServer",
        host: str = "127.0.0.1",
        port: int = 8000,
        workers: int = 1,
        log_level: Literal["debug", "info", "warning", "error"] = "info",
    ) -> None:
        """Run the server."""
        if not (MIN_PORT <= port <= MAX_PORT):
            msg = "Port must be between 1024 and 65535"
            raise ValueError(msg)

        if workers < 1:
            msg = "Workers must be greater than 0"
            raise ValueError(msg)
