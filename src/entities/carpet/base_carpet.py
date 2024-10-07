from dataclasses import dataclass, field
from typing import NewType
from uuid import UUID

from src.entities.category.category import Category

BaseCarpetId = NewType("BaseCarpetId", UUID)


@dataclass
class BaseCarpet:
    base_carpet_id: BaseCarpetId
    title: str
    description: str | None = None,
