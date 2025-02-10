from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from app.application.common.view_models import PatternDTO


class PatternGateway(Protocol):

    @abstractmethod
    async def with_id(self, pattern_id: UUID) -> PatternDTO | None:
        raise NotImplementedError
