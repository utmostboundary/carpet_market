from abc import abstractmethod
from typing import Protocol

from src.domain.common.uow_tracker import UoWTracker


class UoWCommitter(Protocol):

    @abstractmethod
    async def commit(self):
        raise NotImplementedError


class UnitOfWork(UoWTracker, UoWCommitter, Protocol): ...
