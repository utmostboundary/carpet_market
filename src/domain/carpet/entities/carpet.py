from dataclasses import dataclass
from uuid import UUID

from src.domain.carpet.value_objects.color import Color
from src.domain.carpet.value_objects.size import Size
from src.domain.common.entities.entity import DomainEntity


@dataclass
class Carpet(DomainEntity):
    id: UUID
    title: str
    description: str | None
    color: Color
    size: Size
    pattern: str