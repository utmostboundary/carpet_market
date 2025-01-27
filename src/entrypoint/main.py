import os

from fastapi import FastAPI
from dishka.integrations import fastapi as fastapi_integration

from src.entrypoint.ioc import setup_di, ConnectionString
from src.presentation.http.main import setup_routers


def get_db_connection_string() -> ConnectionString:
    return os.environ.get("DB_CONNECTION_STRING")


def create_fastapi_app():
    fastapi_app = FastAPI()

    db_connection_string = get_db_connection_string()

    context = {
        ConnectionString: db_connection_string,
    }

    container = setup_di(context=context)
    fastapi_integration.setup_dishka(container, fastapi_app)
    setup_routers(app=fastapi_app)

    return fastapi_app
