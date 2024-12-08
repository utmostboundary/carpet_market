from fastapi import FastAPI
from dishka.integrations import fastapi as fastapi_integration

from src.infrastructure.bootstrap.ioc import setup_di


def create_fastapi_app():
    fastapi_app = FastAPI()
    container = setup_di()
    fastapi_integration.setup_dishka(container, fastapi_app)
    return fastapi_app
