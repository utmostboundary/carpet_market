from dataclasses import dataclass
from decimal import Decimal
from uuid import UUID

from app.application.common.file_manager import file_path_creator
from app.application.common.input_data import FileMetadata
from app.application.common.uow import UoWCommitter
from app.domain.exceptions.pattern import PatternDoesNotExistError
from app.domain.repositories.carpet import CarpetRepository
from app.domain.repositories.pattern import PatternRepository
from app.domain.value_objects.price import Price
from app.domain.value_objects.quantity import Quantity
from app.domain.value_objects.size import Size


@dataclass(frozen=True)
class AddCarpetCommand:
    pattern_id: UUID
    title: str
    description: str | None
    width: int
    height: int
    base_price: Decimal
    retail_price: Decimal
    stock_amount: int
    main_image: FileMetadata
    images: list[FileMetadata]


class AddCarpet:

    def __init__(
        self,
        pattern_repository: PatternRepository,
        carpet_repository: CarpetRepository,
        committer: UoWCommitter,
    ):
        self._pattern_repository = pattern_repository
        self._carpet_repository = carpet_repository
        self._committer = committer

    async def execute(self, command: AddCarpetCommand) -> UUID:
        pattern = await self._pattern_repository.with_id(pattern_id=command.pattern_id)
        if not pattern:
            raise PatternDoesNotExistError()

        size = Size(width=command.width, height=command.height)
        base_price = Price(value=command.base_price)
        retail_price = Price(value=command.retail_price)
        stock_amount = Quantity(value=command.stock_amount)
        main_image_path = file_path_creator(extension=command.main_image.extension)
        image_paths = [
            file_path_creator(extension=image.extension) for image in command.images
        ]
        pattern_carpets = await self._carpet_repository.with_pattern_id(
            pattern_id=pattern.id
        )
        new_carpet = pattern.add_carpet(
            pattern_carpets=pattern_carpets,
            title=command.title.strip(),
            description=command.description,
            size=size,
            base_price=base_price,
            retail_price=retail_price,
            stock_amount=stock_amount,
            main_image_path=main_image_path,
            image_paths=image_paths,
        )
        await self._committer.commit()
        return new_carpet.id
