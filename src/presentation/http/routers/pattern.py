from dishka.integrations.fastapi import inject, FromDishka
from fastapi import APIRouter, HTTPException

from src.application.operations.commands.pattern.create import (
    CreatePatternCommand,
    CreatePattern,
)
from src.domain.exceptions.base import DomainError

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
