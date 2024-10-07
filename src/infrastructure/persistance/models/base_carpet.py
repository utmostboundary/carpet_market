import sqlalchemy as sa

from src.infrastructure.persistance.models.base import mapper_registry

base_carpet_table = sa.Table(
    "base_carpets",
    mapper_registry.metadata,
    sa.Column("base_carpet_id", sa.UUID, primary_key=True),
    sa.Column("title", sa.String(255), nullable=False),
    sa.Column("description", sa.String(), nullable=True),

)