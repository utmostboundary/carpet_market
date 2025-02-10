from dataclasses import dataclass

from app.domain.exceptions.size import WrongWidthError, WrongHeightError
from app.domain.value_objects.base import BaseValueObject


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
