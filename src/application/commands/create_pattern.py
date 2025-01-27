from dataclasses import dataclass
from uuid import UUID

from src.application.common.uow import UoWCommitter
from src.domain.factories.pattern import PatternFactory
from src.domain.repositories.pattern import PatternRepository


@dataclass(frozen=True)
class CreatePatternCommand:
    title: str
    description: str | None
    color: str
    pile_structure: str
    image_paths: list[str]


class CreatePattern:
    def __init__(
        self,
        pattern_factory: PatternFactory,
        pattern_repository: PatternRepository,
        committer: UoWCommitter,
    ) -> None:
        self._pattern_factory = pattern_factory
        self._committer = committer
        self._pattern_repository = pattern_repository

    async def execute(self, command: CreatePatternCommand) -> UUID:
        pattern = self._pattern_factory.create(
            title=command.title,
            color=command.color,
            pile_structure=command.pile_structure,
            description=command.description,
        )
        self._pattern_repository.add(pattern=pattern)
        await self._committer.commit()
        return pattern.id
