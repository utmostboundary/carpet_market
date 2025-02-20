from uuid import UUID

from app.application.gateways.pattern import PatternGateway
from app.application.view_models.pattern import PatternDTO
from app.domain.exceptions.pattern import PatternDoesNotExistError


class GetPatternById:

    def __init__(self, pattern_gateway: PatternGateway):
        self._pattern_gateway = pattern_gateway

    async def execute(self, pattern_id: UUID) -> PatternDTO:
        pattern_dto = await self._pattern_gateway.with_id(pattern_id=pattern_id)
        if not pattern_dto:
            raise PatternDoesNotExistError()
        return pattern_dto
