from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from app.application.view_models.pattern import PatternDTO, ColorDTO


class PatternGateway(Protocol):

    @abstractmethod
    async def with_id(self, pattern_id: UUID) -> PatternDTO | None:
        raise NotImplementedError

    @abstractmethod
    async def all_colors(self) -> list[ColorDTO]:
        raise NotImplementedError
