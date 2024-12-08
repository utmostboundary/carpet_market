from sqlalchemy.ext.asyncio import AsyncConnection

from src.application.common.commiter import Commiter
from src.application.common.uow_tracker import UoWTracker
from src.domain.common.entities.entity import DomainEntity
from src.infrastructure.persistence.registry import Registry


class UoWTrackerImpl(UoWTracker, Commiter):

    def __init__(
        self,
        registry: Registry,
        connection: AsyncConnection,
    ):
        self._new = {}
        self._dirty = {}
        self._deleted = {}

        self._registry = registry
        self._connection = connection

    def register_new(self, entity: DomainEntity):
        self._new.setdefault(type(entity), []).append(entity)

    def register_dirty(self, entity: DomainEntity):
        self._dirty.setdefault(type(entity), []).append(entity)

    def register_deleted(self, entity: DomainEntity):
        self._deleted.setdefault(type(entity), []).append(entity)

    async def commit(self):
        for entity_type, data in self._new.items():
            mapper = self._registry.get(entity_type=entity_type)
            await mapper.save_all()

        for entity_type, data in self._dirty.items():
            mapper = self._registry.get(entity_type=entity_type)
            await mapper.update_all()

        for entity_type, data in self._deleted.items():
            mapper = self._registry.get(entity_type=entity_type)
            await mapper.delete_all()

        await self._connection.commit()

        self._new.clear()
        self._dirty.clear()
        self._deleted.clear()
