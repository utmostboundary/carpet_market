from dataclasses import dataclass
from decimal import Decimal

from app.domain.exceptions.price import WrongPriceValueError
from app.domain.value_objects.base import BaseValueObject


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

    def __eq__(self, other: "Price") -> bool:
        if self.value == other.value:
            return True
        return False
