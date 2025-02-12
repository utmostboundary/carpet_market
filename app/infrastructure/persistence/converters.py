from typing import Sequence, Mapping, Optional

from sqlalchemy import RowMapping

from app.application.common.uow import UnitOfWork
from app.domain.models.carpet import Carpet
from app.domain.models.pattern import Pattern, Region
from app.domain.value_objects.price import Price
from app.domain.value_objects.quantity import Quantity
from app.domain.value_objects.size import Size


def convert_to_many_carpet_entities(
    rows: Sequence[Mapping],
    uow: UnitOfWork,
) -> list[Carpet]:
    if not rows:
        return []

    carpets = [
        Carpet(
            title=row["title"],
            uow=uow,
            description=row["description"],
            size=Size(width=row["width"], height=row["height"]),
            base_price=Price(value=row["base_price"]),
            retail_price=Price(value=row["retail_price"]),
            stock_amount=Quantity(value=row["stock_amount"]),
            main_image_path=row["main_image_path"],
            image_paths=row["image_paths"],
            pattern_id=row["pattern_id"],
        )
        for row in rows
    ]
    return carpets


def convert_to_pattern_entity(
    row: Optional[RowMapping],
    uow: UnitOfWork,
) -> Pattern | None:
    if not row:
        return None

    pattern = Pattern(
        title=row["title"],
        description=row.get("description", None),
        color=row["color"],
        pile_structure=row["pile_structure"],
        region=Region(row["region"]),
        uow=uow,
    )
    return pattern
