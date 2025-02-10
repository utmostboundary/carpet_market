from decimal import Decimal

import pytest

from app.domain.exceptions.price import WrongPriceValueError
from app.domain.value_objects.price import Price


@pytest.mark.domain
@pytest.mark.value_objects
@pytest.mark.parametrize(
    ["value", "exc_class"],
    [
        (Decimal("100"), None),
        (Decimal("-100"), WrongPriceValueError),
    ],
)
def test_price_validation(value: Decimal, exc_class) -> None:
    if exc_class:
        with pytest.raises(exc_class):
            Price(value=value)
    else:
        price = Price(value=value)

        assert value == price.value
        assert isinstance(price, Price)


def test_prices_are_equal():
    price1 = Price(value=Decimal("100"))
    price2 = Price(value=Decimal("100"))

    assert price1 == price2


def test_prices_are_not_equal():
    price1 = Price(value=Decimal("200"))
    price2 = Price(value=Decimal("100"))

    assert price1 != price2
