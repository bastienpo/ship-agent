"""FastAgent API."""

from abc import ABC, abstractmethod


class FastAgentAPI(ABC):
    """FastAgent API."""

    @abstractmethod
    def setup(self) -> None:
        """Setup the API."""
        pass
