from dishka import Provider, Scope, AsyncContainer, make_async_container

from src.infrastructure.bootstrap.configs import load_all_configs
from src.infrastructure.persistence.config import DBConfig
from src.infrastructure.persistence.provider import (
    get_engine,
    get_connection,
)


def config_provider() -> Provider:
    provider = Provider()

    config = load_all_configs()

    provider.provide(lambda: config.db, scope=Scope.APP, provides=DBConfig)

    return provider


def db_provider() -> Provider:
    provider = Provider()

    provider.provide(get_engine, scope=Scope.APP)
    provider.provide(get_connection, scope=Scope.REQUEST)

    return provider


def setup_providers() -> list[Provider]:
    providers = [
        db_provider(),
        config_provider(),
    ]

    return providers


def setup_di() -> AsyncContainer:
    providers = setup_providers()

    container = make_async_container(*providers)

    return container
