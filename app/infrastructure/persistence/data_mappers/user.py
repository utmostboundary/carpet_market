from typing import Iterable

from sqlalchemy import insert, update, bindparam, delete
from sqlalchemy.ext.asyncio import AsyncConnection

from app.domain.models.user import User
from app.infrastructure.persistence.data_mappers.generic import GenericDataMapper
from app.infrastructure.persistence.tables import user_table


class UserMapperSAImpl(GenericDataMapper[User]):

    def __init__(self, connection: AsyncConnection):
        self._connection = connection

    async def save(self, entities: Iterable[User]) -> None:
        data_to_insert = [
            {
                "id": entity.id,
                "tg_id": entity.tg_contacts.tg_id,
                "tg_username": entity.tg_contacts.tg_username,
                "hashed_password": entity.hashed_password,
                "role": entity.role.value,
                "phone_number": entity.phone_number,
                "is_active": entity.is_active,
            }
            for entity in entities
        ]
        query = insert(user_table)
        await self._connection.execute(query, data_to_insert)

    async def update(self, entities: Iterable[User]) -> None:
        data_to_update = [
            {
                "id": entity.id,
                "tg_id": entity.tg_contacts.tg_id,
                "tg_username": entity.tg_contacts.tg_username,
                "hashed_password": entity.hashed_password,
                "role": entity.role.value,
                "phone_number": entity.phone_number,
                "is_active": entity.is_active,
            }
            for entity in entities
        ]
        query = (
            update(user_table)
            .values(
                tg_id=bindparam("tg_id"),
                tg_username=bindparam("tg_username"),
                hashed_password=bindparam("hashed_password"),
                role=bindparam("role"),
                phone_number=bindparam("phone_number"),
                is_active=bindparam("is_active"),
            )
            .where(user_table.c.id == bindparam("id"))
        )
        await self._connection.execute(query, data_to_update)

    async def delete(self, entities: Iterable[User]) -> None:
        data_to_delete = [entity.id for entity in entities]
        query = delete(user_table).where(user_table.c.id.in_(data_to_delete))
        await self._connection.execute(query)
