from src.domain.models.base import DomainEntity


class User(DomainEntity):
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    telegram_username: str | None = None
    telegram_id: str | None = None
    phone_number: str | None = None
    is_active: bool = True
