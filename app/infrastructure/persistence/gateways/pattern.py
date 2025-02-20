from typing import Optional, Sequence
from uuid import UUID

from sqlalchemy import select, RowMapping
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.view_models.pattern import PatternDTO, ColorDTO
from app.application.gateways.pattern import PatternGateway
from app.infrastructure.persistence.tables import pattern_table


class PatternGatewaySAImpl(PatternGateway):

    def __init__(self, connection: AsyncConnection):
        self._connection = connection

    def _load_pattern_dto(self, row: Optional[RowMapping]) -> PatternDTO | None:
        if not row:
            return None
        return PatternDTO(
            id=row["id"],
            title=row["title"],
            description=row["description"],
            color=row["color"],
            pile_structure=row["pile_structure"],
            region=row["region"],
        )

    def _load_color_dtos(self, rows: Sequence[RowMapping]) -> list[ColorDTO]:
        return [ColorDTO(title=row["color"]) for row in rows]

    async def with_id(self, pattern_id: UUID) -> PatternDTO | None:
        stmt = select(pattern_table).where(pattern_table.c.id == pattern_id)
        result = await self._connection.execute(statement=stmt)
        return self._load_pattern_dto(row=result.mappings().first())

    async def all_colors(self) -> list[ColorDTO]:
        stmt = select(pattern_table.c.color.label("color")).distinct()
        result = await self._connection.execute(statement=stmt)
        return self._load_color_dtos(rows=result.mappings().all())
