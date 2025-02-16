from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True)
class PatternDTO:
    id: UUID
    description: str | None
    color: str
    pile_structure: str
    region: str
