from decimal import Decimal
from typing import Annotated
from uuid import UUID

from dishka.integrations.fastapi import inject, FromDishka
from fastapi import APIRouter, HTTPException, Form, UploadFile, File

from src.application.operations.commands import AddCarpetCommand, AddCarpet
from src.application.common.input_data import FileMetadata
from src.domain.exceptions.base import DomainError

router = APIRouter(prefix="/carpets", tags=["Carpets"])


@router.post("/", response_model=None)
@inject
async def add_carpet(
    handler: FromDishka[AddCarpet],
    pattern_id: Annotated[UUID, Form()],
    title: Annotated[str, Form()],
    description: Annotated[str | None, Form()],
    width: Annotated[int, Form()],
    height: Annotated[int, Form()],
    base_price: Annotated[Decimal, Form()],
    retail_price: Annotated[Decimal, Form()],
    stock_amount: Annotated[int, Form()],
    main_image: Annotated[UploadFile, File()],
    images: Annotated[list[UploadFile], File()],
):
    try:
        result = await handler.execute(
            command=AddCarpetCommand(
                pattern_id=pattern_id,
                title=title,
                description=description,
                width=width,
                height=height,
                base_price=base_price,
                retail_price=retail_price,
                stock_amount=stock_amount,
                main_image=FileMetadata(
                    payload=main_image.file,
                    extension=main_image.filename.split(".")[-1],
                ),
                images=[
                    FileMetadata(
                        payload=image.file, extension=image.filename.split(".")[-1]
                    )
                    for image in images
                ],
            )
        )
    except DomainError as e:
        raise HTTPException(status_code=400, detail=e.message)
    return {"success": True, "id": result}
