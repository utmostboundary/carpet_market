from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.common.uow import UnitOfWork
from app.domain.models.carpet import Carpet
from app.domain.repositories.carpet import CarpetRepository
from app.infrastructure.persistence.converters import convert_to_many_carpet_entities
from app.infrastructure.persistence.tables import carpet_table


class CarpetRepositorySAImpl(CarpetRepository):

    def __init__(self, connection: AsyncConnection, uow: UnitOfWork):
        self._connection = connection
        self._uow = uow

    async def with_pattern_id(self, pattern_id: UUID) -> list[Carpet]:
        stmt = select(
            carpet_table.c.id.label("id"),
            carpet_table.c.description.label("description"),
            carpet_table.c.width.label("width"),
            carpet_table.c.height.label("height"),
            carpet_table.c.base_price.label("base_price"),
            carpet_table.c.retail_price.label("retail_price"),
            carpet_table.c.stock_amount.label("stock_amount"),
            carpet_table.c.main_image_path.label("main_image_path"),
            carpet_table.c.image_paths.label("image_paths"),
            carpet_table.c.pattern_id.label("pattern_id"),
        ).where(carpet_table.c.pattern_id == pattern_id)

        result = await self._connection.execute(statement=stmt)
        return convert_to_many_carpet_entities(
            rows=result.mappings().all(), uow=self._uow
        )
