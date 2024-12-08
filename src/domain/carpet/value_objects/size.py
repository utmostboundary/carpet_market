from dataclasses import dataclass
from decimal import Decimal

from src.domain.common.exceptions.base import DomainError
from src.domain.common.value_objects.base import BaseValueObject


@dataclass(eq=False)
class WrongSizeValueError(DomainError):
    value: Decimal
    text: str

    @property
    def message(self) -> str:
        return self.text


class WrongWidthError(WrongSizeValueError):
    pass


class WrongHeightError(WrongSizeValueError):
    pass


@dataclass(frozen=True)
class Size(BaseValueObject):
    width: Decimal
    height: Decimal

    def _validate(self) -> None:
        if self.width <= 0:
            raise WrongWidthError(
                value=self.width, text="Width cannot be lesser than 0"
            )

        if self.height <= 0:
            raise WrongHeightError(
                value=self.height, text="Height cannot be lesser than 0"
            )

    def __str__(self):
        return f"{self.width} x {self.height}"
