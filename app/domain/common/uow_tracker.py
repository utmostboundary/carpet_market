from abc import abstractmethod
from typing import Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from app.domain.models.base import DomainEntity


class UoWTracker(Protocol):

    @abstractmethod
    def register_new(self, entity: "DomainEntity") -> None:
        raise NotImplementedError

    @abstractmethod
    def register_dirty(self, entity: "DomainEntity") -> None:
        raise NotImplementedError

    @abstractmethod
    def register_deleted(self, entity: "DomainEntity") -> None:
        raise NotImplementedError
