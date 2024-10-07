from dataclasses import dataclass
from typing import NewType
from uuid import UUID

ColorId = NewType("ColorId", UUID)

@dataclass
class Color:
    color_id: ColorId
    title: str