from abc import ABC, abstractmethod
import typing as t

import hikari
import tanjun


class IEmbed(ABC):
    """Interface for Embed factory"""

    @abstractmethod
    def build(self, **kwargs: dict[t.Any, t.Any]) -> hikari.Embed:
        """Builds an embed from given kwargs.
        kwargs:
                - ctx: required
                - title: optional
                - description: optional
                - fields: optional
                - footer: optional
                - header: optional
                - header_icon: optional
                - thumbnail: optional
                - image: optional
                - color: optional
        Returns:
                - hikari.Embed
        """

    
    @abstractmethod
    def _init(self, **kwargs: dict[t.Any, t.Any]) -> None:
        """Initialize embed values"""
        ...