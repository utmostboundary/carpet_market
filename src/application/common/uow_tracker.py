from abc import ABC, abstractmethod

from src.domain.common.entities.entity import DomainEntity


class UoWTracker(ABC):

    @abstractmethod
    def register_new(self, entity: DomainEntity):
        raise NotImplementedError

    @abstractmethod
    def register_dirty(self, entity: DomainEntity):
        raise NotImplementedError

    @abstractmethod
    def register_deleted(self, entity: DomainEntity):
        raise NotImplementedError
