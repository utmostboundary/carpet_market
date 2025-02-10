import pytest

from app.domain.exceptions.size import WrongWidthError, WrongHeightError
from app.domain.value_objects.size import Size


@pytest.mark.domain
@pytest.mark.value_objects
@pytest.mark.parametrize(
    ["width", "height", "exc_class"],
    [
        (100, 200, None),
        (-10, 200, WrongWidthError),
        (0, 200, WrongWidthError),
        (100, -20, WrongHeightError),
        (100, 0, WrongHeightError),
    ],
)
def test_size_validation(width: int, height: int, exc_class) -> None:
    if exc_class:
        with pytest.raises(exc_class):
            Size(width=width, height=height)
    else:
        size = Size(width=width, height=height)

        assert width == size.width
        assert height == size.height
        assert isinstance(size, Size)


def test_sizes_are_equal() -> None:
    size1 = Size(width=100, height=200)
    size2 = Size(width=100, height=200)

    assert size1 == size2


@pytest.mark.domain
@pytest.mark.value_objects
@pytest.mark.parametrize(
    ["width1", "height1", "width2", "height2"],
    [
        (100, 200, 120, 200),
        (100, 200, 100, 250),
    ],
)
def test_sizes_are_not_equal(
    width1: int,
    height1: int,
    width2: int,
    height2: int,
) -> None:

    size1 = Size(width=width1, height=height1)
    size2 = Size(width=width2, height=height2)

    assert size1 != size2
