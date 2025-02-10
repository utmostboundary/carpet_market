from dataclasses import dataclass


@dataclass(eq=False)
class AppError(Exception):

    @property
    def message(self) -> str:
        return "An app error occurred"


class DomainError(AppError):

    @property
    def message(self) -> str:
        return "A models error occurred"
