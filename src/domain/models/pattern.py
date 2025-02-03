from dataclasses import dataclass
from enum import Enum

from src.domain.models.base import UoWedEntity
from src.domain.models.carpet import Carpet
from src.domain.exceptions.carpet import CarpetWithThisSizeAlreadyExistsError
from src.domain.value_objects.price import Price
from src.domain.value_objects.quantity import Quantity
from src.domain.value_objects.size import Size


class Region(Enum):
    CHINA = "CHINA"
    TIBET = "TIBET"


@dataclass
class Pattern(UoWedEntity):
    title: str
    description: str | None
    color: str
    pile_structure: str
    region: Region

    def add_carpet(
        self,
        title: str,
        pattern_carpets: list[Carpet],
        description: str | None,
        size: Size,
        base_price: Price,
        retail_price: Price,
        stock_amount: Quantity,
        main_image_path: str,
        image_paths: list[str],
    ) -> Carpet:
        for carpet in pattern_carpets:
            if carpet.size == size:
                raise CarpetWithThisSizeAlreadyExistsError(
                    text="The pattern already has this size"
                )
        new_carpet = Carpet.create(
            uow=self.uow,
            title=title,
            description=description,
            size=size,
            base_price=base_price,
            retail_price=retail_price,
            stock_amount=stock_amount,
            main_image_path=main_image_path,
            image_paths=image_paths,
            pattern_id=self.id,
        )
        return new_carpet
