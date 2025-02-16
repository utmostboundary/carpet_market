from typing import Protocol

from app.domain.models.user import User


class ViewManager(Protocol):

    async def greeting_view(self, user: User | None) -> None:
        raise NotImplementedError
