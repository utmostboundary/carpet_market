from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.common.uow import UnitOfWork
from app.domain.models.pattern import Pattern, Region
from app.domain.repositories.pattern import PatternRepository
from app.infrastructure.persistence.converters import convert_to_pattern_entity
from app.infrastructure.persistence.tables import pattern_table


class PatternRepositorySAImpl(PatternRepository):

    def __init__(self, connection: AsyncConnection, uow: UnitOfWork):
        self._connection = connection
        self._uow = uow

    async def with_id(self, pattern_id: UUID) -> Pattern | None:
        stmt = select(
            pattern_table.c.id.label("id"),
            pattern_table.c.description.label("description"),
            pattern_table.c.color.label("color"),
            pattern_table.c.pile_structure.label("pile_structure"),
            pattern_table.c.region.label("region"),
        ).where(pattern_table.c.id == pattern_id)

        result = await self._connection.execute(statement=stmt)
        return convert_to_pattern_entity(row=result.mappings().first(), uow=self._uow)

    async def with_all_attributes(
        self,
        color: str,
        pile_structure: str,
        region: str,
    ) -> Pattern | None:
        stmt = select(
            pattern_table.c.id.label("id"),
            pattern_table.c.description.label("description"),
            pattern_table.c.color.label("color"),
            pattern_table.c.pile_structure.label("pile_structure"),
            pattern_table.c.region.label("region"),
        ).where(
            pattern_table.c.color == color,
            pattern_table.c.pile_structure == pile_structure,
            pattern_table.c.region == region,
        )
        result = await self._connection.execute(statement=stmt)
        return convert_to_pattern_entity(row=result.mappings().first(), uow=self._uow)
