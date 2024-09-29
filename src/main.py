from dishka import make_async_container
from fastapi import FastAPI

from dishka.integrations import fastapi as fastapi_integration

from src.config import Config
from src.infrastructure.ioc import AppProvider

config = Config()

container = make_async_container(AppProvider(), context={Config: config})


def create_fastapi_app():
    fastapi_app = FastAPI()
    fastapi_integration.setup_dishka(
        container=container,
        app=fastapi_app
    )
    return fastapi_app


app = create_fastapi_app()