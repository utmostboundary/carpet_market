from dataclasses import dataclass

from src.domain.common.value_objects.base import BaseValueObject


@dataclass(frozen=True)
class Color(BaseValueObject):
    title: str

    def __str__(self):
        return self.title
