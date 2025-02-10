from uuid import UUID

from src.application.auth.identity_provider import IdentityProvider
from src.application.auth.jwt_token_provider import JwtTokenProvider
from src.domain.models.user import Role, JwtToken
from src.infrastructure.auth.auth_token_gettable import AuthTokenGettable


class HttpIdentityProvider(IdentityProvider):

    def __init__(
        self,
        auth_token_gettable: AuthTokenGettable,
        jwt_token_provider: JwtTokenProvider,
    ):
        self._auth_token_gettable = auth_token_gettable
        self._jwt_token_provider = jwt_token_provider

    async def _introspect(self) -> JwtToken:
        token = self._auth_token_gettable.get_auth_token()
        return await self._jwt_token_provider.validate(token=token)

    async def user_id(self) -> UUID:
        introspection = await self._introspect()
        return introspection.payload.user_id

    async def role(self) -> Role:
        introspection = await self._introspect()
        return introspection.payload.role
