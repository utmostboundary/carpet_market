from dataclasses import dataclass

from app.domain.exceptions.base import DomainError
from app.domain.value_objects.base import BaseValueObject


@dataclass(eq=False)
class WrongSizeValueError(DomainError):
    value: int
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
    width: int
    height: int

    def _validate(self) -> None:
        if self.width <= 0:
            raise WrongWidthError(
                value=self.width,
                text="Width cannot be lesser than 0",
            )

        if self.height <= 0:
            raise WrongHeightError(
                value=self.height,
                text="Height cannot be lesser than 0",
            )

    def __str__(self) -> str:
        return f"{self.width} x {self.height}"

    def __eq__(self, other: "Size") -> bool:
        if self.width == other.width and self.height == other.height:
            return True
        return False
