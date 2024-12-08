import logging
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    AsyncConnection,
)

from src.infrastructure.persistence.config import DBConfig


async def get_engine(settings: DBConfig) -> AsyncGenerator[AsyncEngine, None]:
    engine = create_async_engine(
        url=settings.get_connection_url(),
        pool_size=10,
        max_overflow=10,
    )

    logging.info("Engine was created.")

    yield engine

    await engine.dispose()

    logging.info("Engine was disposed.")


async def get_connection(engine: AsyncEngine) -> AsyncConnection:
    async with engine.connect() as connection:
        yield connection

        logging.info("Connection established.")
