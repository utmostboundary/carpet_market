from typing import Sequence, Mapping

from src.application.common.uow import UnitOfWork
from src.domain.models.carpet import Carpet
from src.domain.models.pattern import Pattern
from src.domain.value_objects.price import Price
from src.domain.value_objects.quantity import Quantity
from src.domain.value_objects.size import Size


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
    rows: Sequence[Mapping],
    uow: UnitOfWork,
) -> Pattern | None:
    if not rows:
        return None

    first_row = rows[0]
    pattern = Pattern(
        title=first_row["title"],
        description=first_row.get("description", None),
        color=first_row["color"],
        pile_structure=first_row["pile_structure"],
        region=first_row["region"],
        uow=uow,
    )
    return pattern
