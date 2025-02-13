import pytest

from app.domain.common.uow_tracker import UoWTracker
from app.domain.exceptions.user import DefaultUserMustHaveTgId
from app.domain.models.user import Role, User


@pytest.mark.domain
@pytest.mark.models
@pytest.mark.parametrize(
    ["hashed_password", "tg_id", "role", "phone_number", "exc_class"],
    [
        ("test_hashed", "12345", Role.DEFAULT, "88005555555", None),
        ("test_hashed", None, Role.ADMIN, "88005555555", None),
        ("test_hashed", None, Role.DEFAULT, "88005555555", DefaultUserMustHaveTgId),
    ],
)
def test_create_user(
    uow_tracker: UoWTracker,
    hashed_password: str,
    tg_id: str | None,
    role: Role,
    phone_number: str | None,
    exc_class,
) -> None:
    if exc_class:
        with pytest.raises(exc_class):
            User.create(
                uow=uow_tracker,
                hashed_password=hashed_password,
                tg_id=tg_id,
                role=role,
                phone_number=phone_number,
            )
    else:
        user = User.create(
            uow=uow_tracker,
            hashed_password=hashed_password,
            tg_id=tg_id,
            role=role,
            phone_number=phone_number,
        )

        assert isinstance(user, User)
        assert user.hashed_password == hashed_password
        assert user.role == role
        assert user.tg_id == tg_id
        assert user.phone_number == phone_number
        assert user.is_active == True
