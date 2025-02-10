from dataclasses import dataclass
from uuid import UUID

from app.application.common.uow import UoWCommitter
from app.domain.exceptions.pattern import PatternDoesNotExistError, PatternAlreadyExists
from app.domain.models.pattern import Region
from app.domain.repositories.pattern import PatternRepository


@dataclass(frozen=True)
class EditPatternCommand:
    title: str
    description: str | None
    color: str
    pile_structure: str
    region: Region


class EditPattern:

    def __init__(
        self,
        repository: PatternRepository,
        committer: UoWCommitter,
    ) -> None:
        self._repository = repository
        self._committer = committer

    async def execute(self, pattern_id: UUID, command: EditPatternCommand) -> UUID:
        pattern = await self._repository.with_id(pattern_id=pattern_id)
        if not pattern:
            raise PatternDoesNotExistError()

        duplicate_pattern = await self._repository.with_all_attributes(
            color=command.color,
            pile_structure=command.pile_structure,
            region=command.region,
        )
        if duplicate_pattern and duplicate_pattern.id != pattern.id:
            raise PatternAlreadyExists()

        pattern.update(
            new_title=command.title,
            new_color=command.color,
            new_pile_structure=command.pile_structure,
            new_region=command.region,
            new_description=command.description,
        )

        return pattern.id
