import typing as t
from abc import ABC, abstractmethod

_IBotT = t.TypeVar("_IBotT", bound="IBot")

class IBot(ABC):
    """Interface class for Bot"""

    @abstractmethod
    def create_client(self: _IBotT) -> None:
        """Bind a client to the Bot"""
        pass

    @abstractmethod
    def run(self: _IBotT) -> None:
        """Binds the client to the Bot and subscribs to Events"""
        pass

    @abstractmethod
    async def on_starting(self: _IBotT, event: hikari.StartingEvent) -> None:
        """Runs before bot is connected. Blocks on_started until complete."""
        pass

    @abstractmethod
    async def on_started(self: _IBotT, event: hikari.StartedEvent) -> None:
        """Runs once bot is fully connected"""
        pass

    @abstractmethod
    async def on_stopping(self: _IBotT, event: hikari.StoppingEvent) -> None:
        """Runs at the beginning of shutdown sequence"""
        pass