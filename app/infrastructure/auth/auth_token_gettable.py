from abc import abstractmethod
from typing import Protocol


class AuthTokenGettable(Protocol):

    @abstractmethod
    def get_auth_token(self):
        raise NotImplementedError
