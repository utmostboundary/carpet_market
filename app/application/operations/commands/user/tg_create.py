from dataclasses import dataclass

from app.application.auth.identity_provider import IdentityProvider
from app.application.common.uow import UnitOfWork
from app.application.common.view_manager import ViewManager
from app.domain.models.user import User
from app.domain.value_objects.tg_contacts import TgContacts


@dataclass(frozen=True)
class TgCreateUserCommand:
    tg_id: str
    tg_username: str | None


class TgCreateUser:

    def __init__(
        self,
        identity_provider: IdentityProvider,
        uow: UnitOfWork,
        view_manager: ViewManager,
    ):
        self._identity_provider = identity_provider
        self._uow = uow
        self._view_manager = view_manager

    async def execute(self, command: TgCreateUserCommand) -> None:
        user = await self._identity_provider.get_user()

        if not user:
            User.create(
                uow=self._uow,
                tg_contacts=TgContacts(
                    tg_id=command.tg_id,
                    tg_username=command.tg_username,
                ),
            )

        await self._uow.commit()
