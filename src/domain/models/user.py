from src.domain.models.base import DomainEntity


class Role:
    ADMIN = "ADMIN"
    DEFAULT = "DEFAULT"


class User(DomainEntity):
    hashed_password: str
