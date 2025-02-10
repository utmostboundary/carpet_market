from typing import Iterable

from sqlalchemy import insert, update, bindparam, delete
from sqlalchemy.ext.asyncio import AsyncConnection

from app.domain.models.carpet import Carpet
from app.infrastructure.persistence.data_mappers.generic import GenericDataMapper
from app.infrastructure.persistence.tables import carpet_table


class CarpetMapperSAImpl(GenericDataMapper[Carpet]):

    def __init__(self, connection: AsyncConnection):
        self._connection = connection

    async def save(self, entities: Iterable[Carpet]) -> None:
        data_to_insert = [
            {
                "id": entity.id,
                "description": entity.description,
                "title": entity.title,
                "width": entity.size.width,
                "height": entity.size.height,
                "base_price": entity.base_price,
                "retail_price": entity.retail_price,
                "stock_amount": entity.stock_amount,
                "main_image_path": entity.main_image_path,
            }
            for entity in entities
        ]
        query = insert(carpet_table)
        await self._connection.execute(query, data_to_insert)

    async def update(self, entities: Iterable[Carpet]) -> None:
        data_to_update = [
            {
                "id": entity.id,
                "title": entity.title,
                "description": entity.description,
                "width": entity.size.width,
                "height": entity.size.height,
                "base_price": entity.base_price,
                "retail_price": entity.retail_price,
                "stock_amount": entity.stock_amount,
                "main_image_path": entity.main_image_path,
            }
            for entity in entities
        ]
        query = (
            update(carpet_table)
            .values(
                title=bindparam("title"),
                description=bindparam("description"),
                width=bindparam("width"),
                height=bindparam("height"),
                base_price=bindparam("base_price"),
                retail_price=bindparam("retail_price"),
                stock_amount=bindparam("stock_amount"),
                main_image_path=bindparam("main_image_path"),
            )
            .where(carpet_table.c.id == bindparam("id"))
        )

        await self._connection.execute(query, data_to_update)

    async def delete(self, entities: Iterable[Carpet]) -> None:
        data_to_delete = [entity.id for entity in entities]
        query = delete(carpet_table).where(carpet_table.c.id.in_(data_to_delete))
        await self._connection.execute(query)
