from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncConnection

from src.application.common.uow import UnitOfWork
from src.domain.models.pattern import Pattern
from src.domain.repositories.pattern import PatternRepository
from src.infrastructure.persistence.converters import convert_to_pattern_entity
from src.infrastructure.persistence.tables import pattern_table


class PatternRepositorySAImpl(PatternRepository):

    def __init__(self, connection: AsyncConnection, uow: UnitOfWork):
        self._connection = connection
        self._uow = uow

    def add(self, pattern: Pattern) -> None:
        self._uow.register_new(entity=pattern)

    async def with_id(self, pattern_id: UUID) -> Pattern | None:
        stmt = select(
            pattern_table.c.id.label("id"),
            pattern_table.c.description.label("description"),
            pattern_table.c.color.label("color"),
            pattern_table.c.pile_structure.label("pile_structure"),
        ).where(pattern_table.c.id == pattern_id)

        result = await self._connection.execute(statement=stmt)
        return convert_to_pattern_entity(rows=result.mappings().all(), uow=self._uow)
