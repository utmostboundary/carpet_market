from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from uuid import UUID

from app.domain.common.uow_tracker import UoWTracker
from app.domain.exceptions.user import DefaultUserMustHaveTgId
from app.domain.models.base import UoWedEntity


class Role(Enum):
    ADMIN = "ADMIN"
    DEFAULT = "DEFAULT"


@dataclass(kw_only=True)
class User(UoWedEntity):
    hashed_password: str
    role: Role = field(default=Role.DEFAULT)
    tg_id: str | None
    phone_number: str | None = None
    is_active: bool = True

    @classmethod
    def create(
        cls,
        uow: UoWTracker,
        hashed_password: str,
        tg_id: str | None,
        role: Role = Role.DEFAULT,
        phone_number: str | None = None,
        is_active: bool = True,
    ) -> "User":
        if role != Role.ADMIN and not tg_id:
            raise DefaultUserMustHaveTgId()
        new_user = cls(
            uow=uow,
            hashed_password=hashed_password,
            tg_id=tg_id,
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
