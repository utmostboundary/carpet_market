import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
from dishka.integrations import fastapi as fastapi_integration

from app.entrypoint.ioc import setup_fastapi_di, ConnectionString
from app.presentation.http.main import setup_routers


def get_db_connection_string() -> ConnectionString:
    return os.environ.get("DB_CONNECTION_STRING")


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await app.state.dishka_container.close()


def create_fastapi_app() -> FastAPI:
    fastapi_app = FastAPI(lifespan=lifespan)

    db_connection_string = get_db_connection_string()

    context = {
        ConnectionString: db_connection_string,
    }

    container = setup_fastapi_di(context=context)
    fastapi_integration.setup_dishka(container, fastapi_app)
    setup_routers(app=fastapi_app)

    return fastapi_app
