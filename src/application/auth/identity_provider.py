from abc import abstractmethod
from typing import Protocol
from uuid import UUID

from src.domain.models.user import Role


class IdentityProvider(Protocol):

    @abstractmethod
    async def user_id(self) -> UUID: ...

    @abstractmethod
    async def role(self) -> Role: ...
