from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.common.uow import UnitOfWork
from app.domain.models.user import User
from app.domain.repositories.user import UserRepository
from app.infrastructure.persistence.converters import convert_to_user_entity
from app.infrastructure.persistence.tables import user_table


class UserRepositorySAImpl(UserRepository):

    def __init__(
        self,
        connection: AsyncConnection,
        uow: UnitOfWork,
    ):
        self._connection = connection
        self._uow = uow

    async def with_id(self, user_id: UUID) -> User | None:
        stmt = select(user_table).where(user_table.c.id == user_id)
        result = await self._connection.execute(stmt)
        return convert_to_user_entity(row=result.mappings().first(), uow=self._uow)

    async def with_tg_id(self, tg_id: str) -> User | None:
        stmt = select(user_table).where(user_table.c.tg_id == tg_id)
        result = await self._connection.execute(stmt)
        return convert_to_user_entity(row=result.mappings().first(), uow=self._uow)
