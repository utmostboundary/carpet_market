from src.domain.common.uow_tracker import UoWTracker
from src.domain.factories.pattern import PatternFactory
from src.domain.models.pattern import Pattern


class PatternFactoryImpl(PatternFactory):

    def __init__(self, uow: UoWTracker):
        self._uow = uow

    def create(
        self,
        title: str,
        color: str,
        pile_structure: str,
        description: str | None = None,
    ) -> Pattern:
        new_pattern = Pattern(
            uow=self._uow,
            title=title,
            description=description,
            color=color,
            pile_structure=pile_structure,
        )
        return new_pattern
