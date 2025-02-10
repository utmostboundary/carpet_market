from dataclasses import dataclass

from app.domain.exceptions.base import DomainError


@dataclass(eq=False)
class WrongQuantityValueError(DomainError):
    value: int
    text: str

    @property
    def message(self) -> str:
        return self.text
