from dataclasses import dataclass

from src.domain.exceptions.base import DomainError
from src.domain.value_objects.base import BaseValueObject


@dataclass(eq=False)
class WrongQuantityValueError(DomainError):
    value: int
    text: str

    @property
    def message(self) -> str:
        return self.text


@dataclass(frozen=True)
class Quantity(BaseValueObject):
    value: int

    def __str__(self):
        return self.value

    def _validate(self) -> None:
        if self.value <= 0:
            raise WrongQuantityValueError(
                value=self.value,
                text="Quantity cannot be lesser than 0",
            )
