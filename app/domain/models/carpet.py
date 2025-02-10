from dataclasses import dataclass
from uuid import UUID

from app.domain.common.uow_tracker import UoWTracker
from app.domain.value_objects.price import Price
from app.domain.value_objects.quantity import Quantity
from app.domain.value_objects.size import Size
from app.domain.models.base import UoWedEntity


@dataclass(kw_only=True)
class Carpet(UoWedEntity):
    title: str
    description: str | None
    size: Size
    base_price: Price
    retail_price: Price
    stock_amount: Quantity
    main_image_path: str
    image_paths: list[str]
    pattern_id: UUID

    @classmethod
    def create(
        cls,
        uow: UoWTracker,
        title: str,
        description: str | None,
        size: Size,
        base_price: Price,
        retail_price: Price,
        stock_amount: Quantity,
        main_image_path: str,
        image_paths: list[str],
        pattern_id: UUID,
    ) -> "Carpet":
        new_carpet = cls(
            uow=uow,
            title=title,
            description=description,
            size=size,
            base_price=base_price,
            retail_price=retail_price,
            stock_amount=stock_amount,
            main_image_path=main_image_path,
            image_paths=image_paths,
            pattern_id=pattern_id,
        )
        new_carpet.mark_new()
        return new_carpet
