import pytest_asyncio
from dishka import make_async_container, AsyncContainer

from app.domain.common.uow_tracker import UoWTracker
from app.entrypoint.common import provide_context
from app.entrypoint.ioc import setup_providers


@pytest_asyncio.fixture
async def container() -> AsyncContainer:
    providers = setup_providers()
    container = make_async_container(*providers, context=provide_context())
    yield container
    await container.close()


@pytest_asyncio.fixture
async def uow_tracker(container: AsyncContainer) -> UoWTracker:
    async with container() as request_container:
        yield await request_container.get(UoWTracker)
