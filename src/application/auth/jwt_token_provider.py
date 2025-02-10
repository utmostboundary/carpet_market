from abc import abstractmethod
from typing import Protocol

from src.domain.models.user import JwtToken, TokenPayload


class JwtTokenProvider(Protocol):

    @abstractmethod
    async def validate(self, token: str) -> JwtToken:
        raise NotImplementedError

    @abstractmethod
    async def create_access_token(self, payload: TokenPayload) -> JwtToken:
        raise NotImplementedError

    @abstractmethod
    async def create_refresh_token(self, payload: TokenPayload) -> JwtToken:
        raise NotImplementedError
