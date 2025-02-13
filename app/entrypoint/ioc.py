from typing import AsyncIterable, AsyncGenerator

from dishka import (
    Provider,
    Scope,
    AsyncContainer,
    make_async_container,
    provide,
    from_context,
    AnyOf,
)
from dishka.integrations.aiogram import AiogramProvider
from dishka.integrations.fastapi import FastapiProvider
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncConnection
from fastapi.requests import Request

from app.application.gateways.pattern import PatternGateway
from app.application.operations.commands.carpet.add_carpet import AddCarpet
from app.application.operations.commands.pattern.create import CreatePattern
from app.application.common.uow import UoWCommitter, UnitOfWork
from app.application.operations.commands.pattern.edit import EditPattern
from app.application.operations.queries.pattern.get_by_id import GetPatternById
from app.domain.common.uow_tracker import UoWTracker
from app.domain.factories.pattern import PatternFactory
from app.domain.repositories.carpet import CarpetRepository
from app.domain.repositories.pattern import PatternRepository
from app.infrastructure.auth.auth_token_gettable import AuthTokenGettable
from app.infrastructure.factories.pattern import PatternFactoryImpl
from app.infrastructure.persistence.gateways.pattern import PatternGatewaySAImpl
from app.infrastructure.persistence.registry import Registry, setup_data_mappers
from app.infrastructure.persistence.repositories.carpet import CarpetRepositorySAImpl
from app.infrastructure.persistence.repositories.pattern import PatternRepositorySAImpl
from app.infrastructure.persistence.uow import UnitOfWorkImpl
from app.presentation.http.auth import FastAPIAuthTokenGettable


type ConnectionString = str


class DatabaseProvider(Provider):
    connection_string = from_context(ConnectionString, scope=Scope.APP)

    @provide(scope=Scope.APP)
    async def provide_engine(
        self,
        connection_string: ConnectionString,
    ) -> AsyncGenerator[AsyncEngine, None]:
        engine = create_async_engine(
            url=connection_string,
            pool_size=10,
            max_overflow=10,
        )
        yield engine

        await engine.dispose()

    @provide(scope=Scope.REQUEST)
    async def provide_connection(
        self,
        engine: AsyncEngine,
    ) -> AsyncIterable[AsyncConnection]:
        async with engine.connect() as connection:
            yield connection


class PersistenceProvider(Provider):

    registry = from_context(Registry, scope=Scope.APP)

    uow = provide(
        UnitOfWorkImpl,
        scope=Scope.REQUEST,
        provides=AnyOf[
            UoWTracker,
            UoWCommitter,
            UnitOfWork,
        ],
    )


class CommandsProvider(Provider):

    create_pattern = provide(
        CreatePattern,
        scope=Scope.REQUEST,
    )
    add_carpet = provide(
        AddCarpet,
        scope=Scope.REQUEST,
    )
    edit_pattern = provide(
        EditPattern,
        scope=Scope.REQUEST,
    )


class QueriesProvider(Provider):

    get_pattern_by_id = provide(
        GetPatternById,
        scope=Scope.REQUEST,
    )


class RepositoriesProvider(Provider):

    pattern_repository = provide(
        PatternRepositorySAImpl,
        scope=Scope.REQUEST,
        provides=PatternRepository,
    )
    carpet_repository = provide(
        CarpetRepositorySAImpl,
        scope=Scope.REQUEST,
        provides=CarpetRepository,
    )


class GatewaysProvider(Provider):

    pattern_gateway = provide(
        PatternGatewaySAImpl,
        scope=Scope.REQUEST,
        provides=PatternGateway,
    )


class FactoriesProvider(Provider):

    pattern_factory = provide(
        PatternFactoryImpl,
        scope=Scope.REQUEST,
        provides=PatternFactory,
    )


class AuthProvider(Provider):

    request = from_context(Request, scope=Scope.REQUEST)

    http_token_gettable = provide(
        FastAPIAuthTokenGettable,
        scope=Scope.REQUEST,
        provides=AuthTokenGettable,
    )


def setup_providers() -> list[Provider]:
    providers = [
        DatabaseProvider(),
        PersistenceProvider(),
        CommandsProvider(),
        QueriesProvider(),
        RepositoriesProvider(),
        GatewaysProvider(),
        FactoriesProvider(),
    ]
    return providers


def setup_fastapi_di(
    context: dict,
) -> AsyncContainer:
    providers = setup_providers()
    providers.append(FastapiProvider())
    setup_data_mappers(registry=context.get(Registry))

    container = make_async_container(
        *providers,
        context=context,
    )
    return container


def setup_aiogram_di(
    context: dict,
) -> AsyncContainer:
    providers = setup_providers()
    providers.append(AiogramProvider())
    setup_data_mappers(registry=context.get(Registry))

    container = make_async_container(
        *providers,
        context=context,
    )
    return container
