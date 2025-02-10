from dataclasses import dataclass

from app.domain.exceptions.quantity import WrongQuantityValueError
from app.domain.value_objects.base import BaseValueObject


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
