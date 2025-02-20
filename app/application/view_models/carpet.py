from dataclasses import dataclass
from uuid import UUID

from marshmallow.fields import Decimal


@dataclass(frozen=True)
class CarpetListDTO:
    id: UUID
    title: str
    description: str | None
    width: int
    height: int
    base_price: Decimal
    retail_price: Decimal
    stock_amount: int
    main_image_path: str
    image_paths: list[str]
    pattern_id: UUID
