from uuid import UUID

from app.application.auth.identity_provider import IdentityProvider
from app.application.auth.jwt_token_provider import JwtTokenProvider
from app.domain.models.user import Role, JwtToken, User
from app.domain.repositories.user import UserRepository
from app.infrastructure.auth.auth_token_gettable import AuthTokenGettable


class HttpIdentityProvider(IdentityProvider):

    def __init__(
        self,
        auth_token_gettable: AuthTokenGettable,
        jwt_token_provider: JwtTokenProvider,
        user_repository: UserRepository,
    ):
        self._auth_token_gettable = auth_token_gettable
        self._jwt_token_provider = jwt_token_provider
        self._user_repository = user_repository

    async def _introspect(self) -> JwtToken:
        token = self._auth_token_gettable.get_auth_token()
        return await self._jwt_token_provider.validate(token=token)

    async def get_user(self) -> User | None:
        introspection = await self._introspect()
        return await self._user_repository.with_id(
            user_id=introspection.payload.user_id
        )

    async def get_role(self) -> Role:
        introspection = await self._introspect()
        return introspection.payload.role
