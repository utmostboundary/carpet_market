from src.domain.common.uow_tracker import UoWTracker
from src.domain.exceptions.pattern import PatternAlreadyExists
from src.domain.factories.pattern import PatternFactory
from src.domain.models.pattern import Region, Pattern
from src.domain.repositories.pattern import PatternRepository


class PatternFactoryImpl(PatternFactory):

    def __init__(
        self,
        repository: PatternRepository,
        uow: UoWTracker,
    ):
        self._repository = repository
        self._uow = uow

    async def create(
        self,
        title: str,
        color: str,
        pile_structure: str,
        region: Region,
        description: str | None = None,
    ) -> Pattern:
        if await self._repository.with_all_attributes(
            color=color,
            pile_structure=pile_structure,
            region=region,
        ):
            raise PatternAlreadyExists()
        new_pattern = Pattern(
            uow=self._uow,
            title=title,
            description=description,
            color=color,
            pile_structure=pile_structure,
            region=region,
        )
        new_pattern.mark_new()
        return new_pattern
