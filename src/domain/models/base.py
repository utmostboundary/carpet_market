from abc import ABC
from dataclasses import dataclass, field
from typing import Union
from uuid import UUID, uuid4

from src.domain.common.uow_tracker import UoWTracker


@dataclass(kw_only=True)
class DomainEntity(ABC):
    id: UUID = field(default_factory=uuid4)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other: Union[object, "DomainEntity"]):
        if not isinstance(other, type(self)) or self.id is None:
            return NotImplemented
        return self.id == other.id


@dataclass
class UoWedEntity(DomainEntity):
    uow: UoWTracker

    def mark_new(self) -> None:
        self.uow.register_new(entity=self)

    def mark_dirty(self) -> None:
        self.uow.register_dirty(entity=self)

    def mark_deleted(self) -> None:
        self.uow.register_deleted(entity=self)
