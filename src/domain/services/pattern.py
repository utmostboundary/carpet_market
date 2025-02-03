from uuid import UUID

from src.domain.exceptions.pattern import PatternAlreadyExists
from src.domain.models.pattern import Region, Pattern
from src.domain.repositories.pattern import PatternRepository


class PatternService:

    def __init__(self, repository: PatternRepository):
        self._repository = repository

    async def update(
        self,
        pattern: Pattern,
        new_pattern_id: UUID,
        new_title: str,
        new_description: str | None,
        new_color: str,
        new_pile_structure: str,
        new_region: Region,
    ):
        if (
            await self._repository.with_all_attributes(
                color=new_color,
                pile_structure=new_pile_structure,
                region=new_region,
            )
            and pattern.id != new_pattern_id
        ):
            raise PatternAlreadyExists()

        pattern.title = new_title
        pattern.description = new_description
        pattern.color = new_color
        pattern.pile_structure = new_pile_structure
        pattern.region = new_region

        pattern.mark_dirty()

        return pattern
