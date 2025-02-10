from abc import abstractmethod
from typing import Protocol, Iterable

from app.domain.models.base import DomainEntity


class GenericDataMapper[EntityT: DomainEntity](Protocol):
    @abstractmethod
    async def save(self, entities: Iterable[EntityT]) -> None:
        raise NotImplementedError

    @abstractmethod
    async def update(self, entities: Iterable[EntityT]) -> None:
        raise NotImplementedError

    @abstractmethod
    async def delete(self, entities: Iterable[EntityT]) -> None:
        raise NotImplementedError
