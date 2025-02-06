from fastapi import HTTPException, Security
from fastapi.security import HTTPBearer as _HTTPBearer, HTTPAuthorizationCredentials
from starlette.authentication import AuthenticationError
from starlette.requests import Request
from starlette.status import HTTP_403_FORBIDDEN

from src.infrastructure.auth.auth_token_gettable import AuthTokenGettable


class HTTPBearer(_HTTPBearer):
    async def __call__(self, request: Request) -> HTTPAuthorizationCredentials | None:
        try:
            return await super().__call__(request)

        except HTTPException as e:
            if e.status_code == HTTP_403_FORBIDDEN:
                raise AuthenticationError("Not authenticated") from None

            raise


AuthRequired = Security(HTTPBearer())


class FastAPIAuthTokenGettable(AuthTokenGettable):
    def __init__(self, request: Request) -> None:
        self._request = request

    def get_auth_token(self) -> str:
        token = self._request.headers.get("Authorization")

        if token is None or not token.startswith("Bearer "):
            raise AuthenticationError("Not authenticated")

        return token.replace("Bearer ", "")
