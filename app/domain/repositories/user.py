from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from app.domain.models.user import User


class UserRepository(Protocol):

    @abstractmethod
    async def with_id(self, user_id: UUID) -> User | None:
        raise NotImplementedError

    @abstractmethod
    async def with_tg_id(self, tg_id: str) -> User | None:
        raise NotImplementedError
