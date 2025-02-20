from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class PatternDTO:
    id: UUID
    title: str
    description: str | None
    color: str
    pile_structure: str
    region: str


@dataclass(frozen=True)
class ColorDTO:
    title: str
