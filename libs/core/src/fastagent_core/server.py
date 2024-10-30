"""FastAgent server."""

import uvicorn
from fastapi import FastAPI

from fastagent_core.api import FastAgentAPI

MIN_PORT = 1024
MAX_PORT = 65535


class FastAgentServer:
    """FastAgent server."""

    app: FastAPI

    def __init__(self, api: FastAgentAPI) -> None:
        """Initialize the server."""

    async def setup_routes(self: "FastAgentServer", app: FastAPI) -> None:
        """Setup routes."""

    async def setup_server(self: "FastAgentServer") -> None:
        """Setup the server."""

    async def setup_middlewares(self: "FastAgentServer") -> None:
        """Setup middlewares."""

    def run(
        self: "FastAgentServer",
        host: str = "127.0.0.1",
        port: int = 8000,
        workers: int = 1,
    ) -> None:
        """Run the server."""
        if not (MIN_PORT <= port <= MAX_PORT):
            msg = "Port must be between 1024 and 65535"
            raise ValueError(msg)

        if workers < 1:
            msg = "Workers must be greater than 0"
            raise ValueError(msg)

        self.app = FastAPI()
        config = uvicorn.Config(app=self.app, host=host, port=port, workers=workers)
        server = uvicorn.Server(config)
        server.run()
