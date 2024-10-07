from dataclasses import dataclass
from decimal import Decimal
from typing import NewType
from uuid import UUID

SizeId = NewType("SizeId", UUID)

@dataclass
class Size:
    size_id: SizeId
    height: Decimal
    width: Decimal