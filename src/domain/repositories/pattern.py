from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from src.domain.models.pattern import Pattern


class PatternRepository(Protocol):

    @abstractmethod
    def add(self, pattern: Pattern) -> None:
        raise NotImplementedError

    @abstractmethod
    async def with_id(self, pattern_id: UUID) -> Pattern | None:
        raise NotImplementedError
