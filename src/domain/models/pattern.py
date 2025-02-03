from dataclasses import dataclass
from enum import Enum

from src.domain.models.base import UoWedEntity


class Region(Enum):
    CHINA = "CHINA"
    TIBET = "TIBET"


@dataclass
class Pattern(UoWedEntity):
    title: str
    description: str | None
    color: str
    pile_structure: str
    region: Region
