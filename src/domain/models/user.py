from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from src.domain.models.base import DomainEntity


class Role:
    ADMIN = "ADMIN"
    DEFAULT = "DEFAULT"


class User(DomainEntity):
    hashed_password: str


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
