from app.application.gateways.pattern import PatternGateway
from app.application.view_models.pattern import ColorDTO


class GetColors:

    def __init__(self, pattern_gateway: PatternGateway):
        self._pattern_gateway = pattern_gateway

    async def execute(self) -> list[ColorDTO]:
        colors = await self._pattern_gateway.all_colors()
        return colors
