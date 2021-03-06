import typing as t
from abc import ABC, abstractmethod

import hikari

from ottbot.abc.iembeds import IEmbeds

_IBotT = t.TypeVar("_IBotT", bound="IBot")


class IBot(ABC):
    """Interface class for the discord Bot"""

    embeds: IEmbeds

    @abstractmethod
    def create_client(self: _IBotT) -> None:
        """Bind a client to the Bot"""
        raise NotImplementedError

    @abstractmethod
    async def on_guild_available(self: _IBotT, event: hikari.GuildAvailableEvent) -> None:
        """Runs when the bot joins a new guild"""
        raise NotImplementedError

    @abstractmethod
    async def on_starting(self: _IBotT, event: hikari.StartingEvent) -> None:
        """Runs before bot is connected. Blocks on_started until complete."""
        raise NotImplementedError

    @abstractmethod
    async def on_started(self: _IBotT, event: hikari.StartedEvent) -> None:
        """Runs once bot is fully connected"""
        raise NotImplementedError

    @abstractmethod
    async def on_stopping(self: _IBotT, event: hikari.StoppingEvent) -> None:
        """Runs at the beginning of shutdown sequence"""
        raise NotImplementedError

    @abstractmethod
    async def on_stopped(self: _IBotT, event: hikari.StoppingEvent) -> None:
        """Runs after the bot has been shutdown"""
        raise NotImplementedError
