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
from dishka.integrations.fastapi import FastapiProvider
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, AsyncConnection
from fastapi.requests import Request

from src.application.operations.commands.carpet.add_carpet import AddCarpet
from src.application.operations.commands.pattern.create import CreatePattern
from src.application.common.uow import UoWCommitter, UnitOfWork
from src.application.operations.commands.pattern.edit import EditPattern
from src.domain.common.uow_tracker import UoWTracker
from src.domain.factories.pattern import PatternFactory
from src.domain.models.carpet import Carpet
from src.domain.models.pattern import Pattern
from src.domain.repositories.carpet import CarpetRepository
from src.domain.repositories.pattern import PatternRepository
from src.domain.services.pattern import PatternService
from src.infrastructure.auth.auth_token_gettable import AuthTokenGettable
from src.infrastructure.factories.pattern import PatternFactoryImpl
from src.infrastructure.persistence.data_mappers.carpet import CarpetMapperSAImpl
from src.infrastructure.persistence.data_mappers.generic import GenericDataMapper
from src.infrastructure.persistence.data_mappers.pattern import PatternMapperSAImpl
from src.infrastructure.persistence.registry import Registry
from src.infrastructure.persistence.repositories.carpet import CarpetRepositorySAImpl
from src.infrastructure.persistence.repositories.pattern import PatternRepositorySAImpl
from src.infrastructure.persistence.uow import UnitOfWorkImpl
from src.presentation.http.auth import FastAPIAuthTokenGettable

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
        print(f"===========================CONNECTED")
        yield engine

        await engine.dispose()
        print(f"===========================DISPOSED")

    @provide(scope=Scope.REQUEST)
    async def provide_connection(
        self,
        engine: AsyncEngine,
    ) -> AsyncIterable[AsyncConnection]:
        async with engine.connect() as connection:
            yield connection


class PersistenceProvider(Provider):

    @provide(scope=Scope.REQUEST)
    async def provide_registry(
        self,
        carpet_mapper: GenericDataMapper[Carpet],
        pattern_mapper: GenericDataMapper[Pattern],
    ) -> Registry:
        registry = Registry()
        registry.add_mapper(mapper=carpet_mapper)
        registry.add_mapper(mapper=pattern_mapper)
        return registry

    uow = provide(
        UnitOfWorkImpl,
        scope=Scope.REQUEST,
        provides=AnyOf[
            UoWTracker,
            UoWCommitter,
            UnitOfWork,
        ],
    )


class DataMappersProvider(Provider):

    pattern_mapper = provide(
        PatternMapperSAImpl,
        scope=Scope.REQUEST,
        provides=GenericDataMapper[Pattern],
    )
    carpet_mapper = provide(
        CarpetMapperSAImpl,
        scope=Scope.REQUEST,
        provides=GenericDataMapper[Carpet],
    )


class InteractorsProvider(Provider):

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


class FactoriesProvider(Provider):

    pattern_factory = provide(
        PatternFactoryImpl,
        scope=Scope.REQUEST,
        provides=PatternFactory,
    )


class ServicesProvider(Provider):

    pattern_service = provide(
        PatternService,
        scope=Scope.REQUEST,
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
        DataMappersProvider(),
        InteractorsProvider(),
        RepositoriesProvider(),
        FactoriesProvider(),
        ServicesProvider(),
    ]
    return providers


def setup_fastapi_di(context: dict) -> AsyncContainer:
    providers = setup_providers()
    providers.append(FastapiProvider())

    container = make_async_container(*providers, context=context)
    return container
