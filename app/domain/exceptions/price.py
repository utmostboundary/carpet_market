from dataclasses import dataclass
from decimal import Decimal

from app.domain.exceptions.base import DomainError


@dataclass(eq=False)
class WrongPriceValueError(DomainError):
    value: Decimal
    text: str

    @property
    def message(self) -> str:
        return self.text
