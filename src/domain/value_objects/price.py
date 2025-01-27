from dataclasses import dataclass
from decimal import Decimal

from src.domain.exceptions.base import DomainError
from src.domain.value_objects.base import BaseValueObject


@dataclass(eq=False)
class WrongPriceValueError(DomainError):
    value: Decimal
    text: str

    @property
    def message(self) -> str:
        return self.text


@dataclass(frozen=True)
class Price(BaseValueObject):
    value: Decimal

    def __str__(self):
        return self.value

    def _validate(self) -> None:
        if self.value <= Decimal("0"):
            raise WrongPriceValueError(
                value=self.value,
                text="Price cannot be lesser than 0",
            )
