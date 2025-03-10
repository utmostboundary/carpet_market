import os

from app.infrastructure.persistence.registry import Registry
from app.entrypoint.ioc import ConnectionString


def get_db_connection_string() -> ConnectionString:
    return os.environ.get("DB_CONNECTION_STRING")


def provide_context() -> dict:
    db_connection_string = get_db_connection_string()
    registry = Registry()
    context = {
        ConnectionString: db_connection_string,
        Registry: registry,
    }
    return context
