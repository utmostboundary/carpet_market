from abc import abstractmethod
from typing import Protocol

from src.domain.models.pattern import Pattern


class PatternFactory(Protocol):

    @abstractmethod
    def create(
        self,
        title: str,
        color: str,
        pile_structure: str,
        description: str | None = None,
    ) -> Pattern:
        raise NotImplementedError
