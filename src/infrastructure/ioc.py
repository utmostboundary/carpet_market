from dishka import Provider, from_context, Scope

from src.config import Config


class AppProvider(Provider):
    config = from_context(provides=Config, scope=Scope.APP)
