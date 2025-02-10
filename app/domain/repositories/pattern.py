from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from app.domain.models.pattern import Pattern, Region


class PatternRepository(Protocol):

    @abstractmethod
    async def with_id(self, pattern_id: UUID) -> Pattern | None:
        raise NotImplementedError

    @abstractmethod
    async def with_all_attributes(
        self,
        color: str,
        pile_structure: str,
        region: Region,
    ) -> Pattern | None:
        raise NotImplementedError
