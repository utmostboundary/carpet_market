from app.application.view_models.carpet import CarpetListDTO
from app.application.gateways.carpet import CarpetGateway


class GetCarpets:

    def __init__(self, carpet_gateway: CarpetGateway):
        self._carpet_gateway = carpet_gateway

    async def execute(self) -> list[CarpetListDTO]:
        carpet_dtos = await self._carpet_gateway.all()
        return carpet_dtos
