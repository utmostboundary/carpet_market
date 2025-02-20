from abc import abstractmethod
from typing import Protocol

from app.application.view_models.carpet import CarpetListDTO


class CarpetGateway(Protocol):

    @abstractmethod
    async def all(self) -> list[CarpetListDTO]:
        raise NotImplementedError
