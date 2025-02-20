from dataclasses import dataclass
from uuid import UUID

from app.application.common.uow import UoWCommitter
from app.domain.factories.pattern import PatternFactory


@dataclass(frozen=True)
class CreatePatternCommand:
    title: str
    description: str | None
    color: str
    pile_structure: str
    region: str


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
            color=command.color.strip(),
            pile_structure=command.pile_structure.strip(),
            region=command.region.strip(),
            description=command.description,
        )
        await self._committer.commit()
        return pattern.id
