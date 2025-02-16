from dataclasses import dataclass

from app.domain.value_objects.base import BaseValueObject


@dataclass(frozen=True)
class TgContacts(BaseValueObject):

    tg_id: str
    tg_username: str | None
