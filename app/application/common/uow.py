from abc import abstractmethod
from typing import Protocol

from app.domain.common.uow_tracker import UoWTracker


class UoWCommitter(Protocol):

    @abstractmethod
    async def commit(self) -> None:
        raise NotImplementedError


class UnitOfWork(UoWTracker, UoWCommitter, Protocol): ...
