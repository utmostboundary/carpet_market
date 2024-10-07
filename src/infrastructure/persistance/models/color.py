import sqlalchemy as sa
from sqlalchemy import UniqueConstraint

from src.entities.carpet.color import Color
from src.infrastructure.persistance.models.base import mapper_registry

color_table = sa.Table(
    "colors",
    mapper_registry.metadata,
    sa.Column("color_id", sa.UUID, primary_key=True),
    sa.Column("title", sa.String(50)),
    sa.Column(
            "created_at",
            sa.DateTime,
            default=sa.func.now(),
            server_default=sa.func.now(),
        ),
    UniqueConstraint("title", name="uq_color_title")
)


def map_color_table() -> None:
    mapper_registry.map_imperatively(
        Color,
        color_table
    )