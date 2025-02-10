from dataclasses import dataclass

from app.domain.exceptions.base import DomainError


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
