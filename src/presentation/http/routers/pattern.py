from uuid import UUID

from dishka.integrations.fastapi import inject, FromDishka
from fastapi import APIRouter, HTTPException

from src.application.operations.commands.pattern.create import (
    CreatePatternCommand,
    CreatePattern,
)
from src.application.operations.commands.pattern.edit import (
    EditPatternCommand,
    EditPattern,
)
from src.domain.exceptions.base import DomainError
from src.domain.exceptions.pattern import PatternDoesNotExistError

router = APIRouter(prefix="/patterns", tags=["Patterns"])


@router.post(
    "/",
)
@inject
async def create_pattern(
    command: CreatePatternCommand,
    handler: FromDishka[CreatePattern],
):
    try:
        result = await handler.execute(command=command)
    except DomainError as e:
        raise HTTPException(status_code=400, detail=e.message)
    return {"success": True, "id": result}


@router.patch("/{pattern_id/")
@inject
async def edit_pattern(
    pattern_id: UUID, command: EditPatternCommand, handler: FromDishka[EditPattern]
):
    try:
        result = await handler.execute(pattern_id=pattern_id, command=command)
    except PatternDoesNotExistError as e:
        raise HTTPException(status_code=404, detail=e.message)
    except DomainError as e:
        raise HTTPException(status_code=400, detail=e.message)

    return {"success": True, "id": result}
