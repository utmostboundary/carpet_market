from dataclasses import dataclass

from src.domain.exceptions.base import DomainError


@dataclass(eq=False)
class PatternDoesNotExistError(DomainError):

    @property
    def message(self) -> str:
        return "Pattern doesn't exist"


@dataclass(eq=False)
class PatternAlreadyExists(DomainError):

    @property
    def message(self) -> str:
        return "Pattern already exists"
