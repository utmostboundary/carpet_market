from typing import Iterable
from uuid import UUID

from app.domain.models.base import DomainEntity
from app.domain.value_objects.price import Price


class OrderLine(DomainEntity):
    carpet_title: str
    price_per_item: Price
    quantity: int


class Order(DomainEntity):
    order_lines: Iterable[OrderLine]
    user_id: UUID
