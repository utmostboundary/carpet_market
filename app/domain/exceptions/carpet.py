from dataclasses import dataclass

from app.domain.exceptions.base import DomainError


@dataclass(eq=False)
class CarpetWithThisSizeAlreadyExistsError(DomainError):
    text: str

    @property
    def message(self) -> str:
        return self.text
