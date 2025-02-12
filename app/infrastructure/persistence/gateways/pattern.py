from typing import Optional
from uuid import UUID

from sqlalchemy import select, RowMapping
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.common.view_models import PatternDTO
from app.application.gateways.pattern import PatternGateway
from app.infrastructure.persistence.tables import pattern_table


class PatternGatewaySAImpl(PatternGateway):

    def __init__(self, connection: AsyncConnection):
        self._connection = connection

    def _load_pattern_dto(self, row: Optional[RowMapping]) -> PatternDTO | None:
        if not row:
            return None
        return PatternDTO(
            id=row.id,
            description=row.description,
            color=row.color,
            pile_structure=row.pile_structure,
            region=row.region,
        )

    async def with_id(self, pattern_id: UUID) -> PatternDTO | None:
        stmt = select(
            pattern_table.c.id.label("id"),
            pattern_table.c.description.label("description"),
            pattern_table.c.color.label("color"),
            pattern_table.c.pile_structure.label("pile_structure"),
            pattern_table.c.region.label("region"),
        ).where(pattern_table.c.id == pattern_id)

        result = await self._connection.execute(statement=stmt)
        return self._load_pattern_dto(row=result.mappings().first())
