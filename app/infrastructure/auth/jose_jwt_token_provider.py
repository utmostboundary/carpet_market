from uuid import UUID

from jose import jwt, JWTError

from app.application.auth.jwt_token_provider import JwtTokenProvider
from app.application.common.clock import Clock
from app.domain.exceptions.user import InvalidTokenError
from app.domain.models.user import JwtToken, TokenPayload
from app.infrastructure.auth.auth_config import AuthConfig


class JoseJwtTokenProvider(JwtTokenProvider):

    def __init__(self, clock: Clock, auth_config: AuthConfig):
        self._clock = clock
        self._auth_config = auth_config

    async def validate(self, token: str) -> JwtToken:
        try:
            credentials = jwt.decode(
                token=token,
                key=self._auth_config.jwt_secret,
                algorithms=["HS256"],
            )
        except JWTError as e:
            raise InvalidTokenError("Invalid token") from e

        expires_in = credentials["exp"]
        created_at = credentials["iat"]

        if expires_in < self._clock.now():
            raise InvalidTokenError("Token expired")

        payload = TokenPayload(
            user_id=UUID(credentials["user_id"]),
            role=credentials["role"],
        )

        return JwtToken(
            value=token,
            payload=payload,
            expires_in=expires_in,
            created_at=created_at,
        )

    async def create_access_token(self, payload: TokenPayload) -> JwtToken:
        now = self._clock.now()
        to_encode = {
            "user_id": payload.user_id,
            "role": payload.role,
            "iat": int(now.timestamp()),
            "exp": int((now + self._auth_config.access_expiration).timestamp()),
        }
        token = jwt.encode(
            claims=to_encode,
            key=self._auth_config.jwt_secret,
            algorithm="HS256",
        )
        return JwtToken(
            value=token,
            payload=payload,
            expires_in=now + self._auth_config.access_expiration,
            created_at=now,
        )

    async def create_refresh_token(self, payload: TokenPayload) -> JwtToken:
        now = self._clock.now()
        to_encode = {
            "user_id": payload.user_id,
            "role": payload.role,
            "iat": int(now.timestamp()),
            "exp": int((now + self._auth_config.access_expiration).timestamp()),
        }
        token = jwt.encode(
            claims=to_encode,
            key=self._auth_config.jwt_secret,
            algorithm="HS256",
        )
        return JwtToken(
            value=token,
            payload=payload,
            expires_in=now + self._auth_config.refresh_expiration,
            created_at=now,
        )
