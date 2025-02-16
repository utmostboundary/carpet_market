from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import UUID

from app.domain.common.uow_tracker import UoWTracker
from app.domain.exceptions.user import AdminMustHavePassword
from app.domain.models.base import UoWedEntity
from app.domain.value_objects.tg_contacts import TgContacts


class Role(Enum):
    ADMIN = "ADMIN"
    DEFAULT = "DEFAULT"


@dataclass(kw_only=True)
class User(UoWedEntity):
    tg_contacts: TgContacts | None
    hashed_password: str | None
    role: Role = field(default=Role.DEFAULT)
    phone_number: str | None = None
    is_active: bool = True

    @classmethod
    def create(
        cls,
        uow: UoWTracker,
        tg_contacts: TgContacts | None,
        hashed_password: str | None = None,
        role: Role = Role.DEFAULT,
        phone_number: str | None = None,
        is_active: bool = True,
    ) -> "User":
        if role == Role.ADMIN and not hashed_password:
            raise AdminMustHavePassword()
        new_user = cls(
            uow=uow,
            tg_contacts=tg_contacts,
            hashed_password=hashed_password,
            role=role,
            phone_number=phone_number,
            is_active=is_active,
        )
        new_user.mark_new()
        return new_user


@dataclass(kw_only=True)
class TokenPayload:
    user_id: UUID
    role: Role


@dataclass(kw_only=True)
class JwtToken:
    value: str
    payload: TokenPayload
    expires_in: datetime
    created_at: datetime
