from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.common.uow import UnitOfWork
from app.domain.models.base import DomainEntity
from app.infrastructure.persistence.registry import Registry


class UnitOfWorkImpl(UnitOfWork):

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

    def register_new(self, entity: DomainEntity) -> None:
        self._new.setdefault(type(entity), []).append(entity)

    def register_dirty(self, entity: DomainEntity) -> None:
        self._dirty.setdefault(type(entity), []).append(entity)

    def register_deleted(self, entity: DomainEntity) -> None:
        self._deleted.setdefault(type(entity), []).append(entity)

    async def _flush(self) -> None:
        for entity_type, data in self._new.items():
            mapper = self._registry.get(
                self._connection,
                entity_type=entity_type,
            )
            await mapper.save(entities=data)

        for entity_type, data in self._dirty.items():
            mapper = self._registry.get(
                self._connection,
                entity_type=entity_type,
            )
            await mapper.update(entities=data)

        for entity_type, data in self._deleted.items():
            mapper = self._registry.get(
                self._connection,
                entity_type=entity_type,
            )
            await mapper.delete(entities=data)

    async def commit(self) -> None:
        await self._flush()
        await self._connection.commit()

        self._new.clear()
        self._dirty.clear()
        self._deleted.clear()
