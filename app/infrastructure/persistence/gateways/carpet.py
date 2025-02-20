from typing import Sequence

from sqlalchemy import RowMapping, select
from sqlalchemy.ext.asyncio import AsyncConnection

from app.application.view_models.carpet import CarpetListDTO
from app.application.gateways.carpet import CarpetGateway
from app.infrastructure.persistence.tables import carpet_table


class CarpetGatewaySAImpl(CarpetGateway):

    def __init__(self, connection: AsyncConnection):
        self._connection = connection

    def _load_carpet_dtos(
        self, rows: Sequence[RowMapping]
    ) -> list[CarpetListDTO] | None:
        return [
            CarpetListDTO(
                id=row["id"],
                title=row["title"],
                description=row.get("description"),
                width=row["width"],
                height=row["height"],
                base_price=row["base_price"],
                retail_price=row["retail_price"],
                stock_amount=row["stock_amount"],
                main_image_path=row["main_image_path"],
                image_paths=row["image_paths"],
                pattern_id=row["pattern_id"],
            )
            for row in rows
        ]

    async def all(self) -> list[CarpetListDTO] | None:
        stmt = select(carpet_table)

        result = await self._connection.execute(statement=stmt)
        return self._load_carpet_dtos(rows=result.mappings().all())
