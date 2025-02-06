from uuid import UUID

from src.domain.common.uow_tracker import UoWTracker
from src.domain.exceptions.carpet import CarpetWithThisSizeAlreadyExistsError
from src.domain.exceptions.pattern import PatternAlreadyExists
from src.domain.models.carpet import Carpet
from src.domain.models.pattern import Region, Pattern
from src.domain.repositories.carpet import CarpetRepository
from src.domain.repositories.pattern import PatternRepository
from src.domain.value_objects.price import Price
from src.domain.value_objects.quantity import Quantity
from src.domain.value_objects.size import Size


class PatternService:

    def __init__(
        self,
        pattern_repository: PatternRepository,
        carpet_repository: CarpetRepository,
        uow: UoWTracker,
    ) -> None:
        self._pattern_repository = pattern_repository
        self._carpet_repository = carpet_repository
        self._uow = uow

    async def add_carpet(
        self,
        pattern_id: UUID,
        title: str,
        description: str | None,
        size: Size,
        base_price: Price,
        retail_price: Price,
        stock_amount: Quantity,
        main_image_path: str,
        image_paths: list[str],
    ) -> Carpet:
        pattern_carpets = await self._carpet_repository.with_pattern_id(
            pattern_id=pattern_id
        )
        for carpet in pattern_carpets:
            if carpet.size == size:
                raise CarpetWithThisSizeAlreadyExistsError(
                    text="The pattern already has this size"
                )
        new_carpet = Carpet.create(
            uow=self._uow,
            title=title,
            description=description,
            size=size,
            base_price=base_price,
            retail_price=retail_price,
            stock_amount=stock_amount,
            main_image_path=main_image_path,
            image_paths=image_paths,
            pattern_id=pattern_id,
        )
        return new_carpet
