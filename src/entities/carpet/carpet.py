from dataclasses import dataclass
from typing import NewType
from uuid import UUID

from src.entities.carpet.base_carpet import BaseCarpetId
from src.entities.carpet.color import ColorId
from src.entities.carpet.size import SizeId

CarpetId = NewType("CarpetId", UUID)


@dataclass
class Carpet:
    carpet_id: CarpetId
    stock_amount: int
    base_carpet_id: BaseCarpetId
    color_id: ColorId
    size_id: SizeId

