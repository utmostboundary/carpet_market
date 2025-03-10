from contextlib import asynccontextmanager

from fastapi import FastAPI
from dishka.integrations import fastapi as fastapi_integration
from fastapi.responses import ORJSONResponse

from app.entrypoint.common import provide_context
from app.entrypoint.ioc import setup_fastapi_di
from app.presentation.http.setup import setup_routers


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    await app.state.dishka_container.close()


def create_fastapi_app() -> FastAPI:
    fastapi_app = FastAPI(
        lifespan=lifespan,
        default_response_class=ORJSONResponse,
    )

    container = setup_fastapi_di(context=provide_context())

    fastapi_integration.setup_dishka(container, fastapi_app)
    setup_routers(app=fastapi_app)

    return fastapi_app
