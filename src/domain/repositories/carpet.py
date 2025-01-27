from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from src.domain.models.carpet import Carpet


class CarpetRepository(Protocol):

    @abstractmethod
    async def with_pattern_id(self, pattern_id: UUID) -> list[Carpet]:
        raise NotImplementedError
