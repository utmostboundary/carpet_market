from abc import abstractmethod
from typing import Protocol

from app.domain.models.user import Role, User


class IdentityProvider(Protocol):

    @abstractmethod
    async def get_user(self) -> User | None:
        raise NotImplementedError

    @abstractmethod
    async def get_role(self) -> Role:
        raise NotImplementedError
