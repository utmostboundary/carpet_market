from fastapi import FastAPI

from src.presentation.http.routers import pattern, carpet


def setup_routers(app: FastAPI) -> None:
    app.include_router(pattern.router, prefix="/api/v1")
    app.include_router(carpet.router, prefix="/api/v1")
