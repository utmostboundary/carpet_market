from dataclasses import dataclass
from uuid import UUID

from app.application.common.uow import UoWCommitter
from app.domain.factories.pattern import PatternFactory
from app.domain.models.pattern import Region


@dataclass(frozen=True)
class CreatePatternCommand:
    title: str
    description: str | None
    color: str
    pile_structure: str
    region: Region


class CreatePattern:

    def __init__(
        self,
        pattern_factory: PatternFactory,
        committer: UoWCommitter,
    ) -> None:
        self._pattern_factory = pattern_factory
        self._committer = committer

    async def execute(self, command: CreatePatternCommand) -> UUID:
        pattern = await self._pattern_factory.create(
            title=command.title,
            color=command.color,
            pile_structure=command.pile_structure,
            region=command.region,
            description=command.description,
        )
        await self._committer.commit()
        return pattern.id
