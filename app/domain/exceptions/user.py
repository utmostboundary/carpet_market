from dataclasses import dataclass

from app.domain.exceptions.base import DomainError


@dataclass(eq=False)
class InvalidTokenError(DomainError):
    text: str

    @property
    def message(self) -> str:
        return self.text


@dataclass(eq=False)
class AdminMustHavePassword(DomainError):

    @property
    def message(self) -> str:
        return "Admin must have password"


@dataclass(eq=False)
class UserDoesNotExist(DomainError):

    @property
    def message(self) -> str:
        return "User does not exist"
