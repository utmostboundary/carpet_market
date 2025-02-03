from abc import abstractmethod
from typing import Protocol

from src.domain.models.pattern import Region


class PatternFactory(Protocol):

    @abstractmethod
    async def create(
        self,
        title: str,
        color: str,
        pile_structure: str,
        region: Region,
        description: str | None = None,
    ): ...
