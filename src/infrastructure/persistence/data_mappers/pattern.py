from typing import Iterable

from sqlalchemy import insert, update, bindparam, delete
from sqlalchemy.ext.asyncio import AsyncConnection

from src.domain.models.pattern import Pattern
from src.infrastructure.persistence.data_mappers.generic import GenericDataMapper
from src.infrastructure.persistence.tables import pattern_table


class PatternMapperSAImpl(GenericDataMapper[Pattern]):

    def __init__(self, connection: AsyncConnection):
        self._connection = connection

    async def save(self, entities: Iterable[Pattern]) -> None:
        data_to_insert = [
            {
                "id": entity.id,
                "description": entity.description,
                "title": entity.title,
                "color": entity.color,
                "pile_structure": entity.pile_structure,
                "image_paths": entity.image_paths,
            }
            for entity in entities
        ]
        print(f"==================DATA TO INSERT {data_to_insert}")
        query = insert(pattern_table)
        await self._connection.execute(query, data_to_insert)

    async def update(self, entities: Iterable[Pattern]) -> None:
        data_to_update = [
            {
                "id": entity.id,
                "title": entity.title,
                "description": entity.description,
                "color": entity.color,
                "pile_structure": entity.pile_structure,
                "image_paths": entity.image_paths,
            }
            for entity in entities
        ]
        query = (
            update(pattern_table)
            .values(
                title=bindparam("title"),
                description=bindparam("description"),
                color=bindparam("color"),
                pile_structure=bindparam("pile_structure"),
                image_paths=bindparam("image_paths"),
            )
            .where(pattern_table.c.id == bindparam("id"))
        )
        await self._connection.execute(query, data_to_update)

    async def delete(self, entities: Iterable[Pattern]) -> None:
        data_to_delete = [entity.id for entity in entities]
        query = delete(pattern_table).where(pattern_table.c.id.in_(data_to_delete))
        await self._connection.execute(query)
