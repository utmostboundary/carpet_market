from dataclasses import dataclass

from app.domain.exceptions.base import DomainError


@dataclass(eq=False)
class InvalidTokenError(DomainError):
    text: str

    @property
    def message(self) -> str:
        return self.text


@dataclass(eq=False)
class DefaultUserMustHaveTgId(DomainError):

    @property
    def message(self) -> str:
        return "User must have Telegram ID"
