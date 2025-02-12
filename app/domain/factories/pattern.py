from abc import abstractmethod
from typing import Protocol

from app.domain.models.pattern import Region, Pattern


class PatternFactory(Protocol):

    @abstractmethod
    async def create(
        self,
        title: str,
        color: str,
        pile_structure: str,
        region: str,
        description: str | None = None,
    ) -> Pattern: ...
