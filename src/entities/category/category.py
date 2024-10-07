from dataclasses import dataclass
from decimal import Decimal
from typing import NewType
from uuid import UUID

from src.entities.carpet.base_carpet import BaseCarpet

CategoryId = NewType("CategoryId", UUID)


@dataclass
class Category:
    category_id: CategoryId
    title: str
    price_per_square_meter: Decimal
    base_carpets: list[BaseCarpet]