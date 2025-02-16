from app.application.common.view_manager import ViewManager
from app.domain.models.user import User


class TgViewManger(ViewManager):

    async def greeting_view(self, user: User | None) -> None:

        if user:
            pass

        else:
            pass
