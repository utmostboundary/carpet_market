from aiogram.types import TelegramObject

from app.application.auth.identity_provider import IdentityProvider
from app.domain.exceptions.user import UserDoesNotExist
from app.domain.models.user import User, Role
from app.domain.repositories.user import UserRepository


class TgIdentityProvider(IdentityProvider):

    def __init__(
        self,
        user_repository: UserRepository,
        tg_update: TelegramObject,
    ):
        self._user_repository = user_repository
        self._tg_update = tg_update

    async def get_user(self) -> User | None:
        user = await self._user_repository.with_tg_id(
            tg_id=str(self._tg_update.from_user.id)
        )
        return user

    async def get_role(self) -> Role:
        user = await self.get_user()
        if not user:
            raise UserDoesNotExist()
        return user.role
