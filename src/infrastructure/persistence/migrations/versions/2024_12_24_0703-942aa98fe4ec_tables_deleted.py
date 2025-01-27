"""tables deleted

Revision ID: 942aa98fe4ec
Revises: 8330a655c2ed
Create Date: 2024-12-24 07:03:28.758491

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = "942aa98fe4ec"
down_revision: Union[str, None] = "8330a655c2ed"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_table("pile_structures")
    op.drop_table("carpets")
    op.drop_table("colors")
    op.drop_table("patterns")


def downgrade() -> None:
    op.create_table(
        "patterns",
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column("title", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("description", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="patterns_pkey"),
    )
    op.create_table(
        "colors",
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column("title", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("pattern_id", sa.UUID(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ["pattern_id"], ["patterns.id"], name="colors_pattern_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="colors_pkey"),
    )
    op.create_table(
        "pile_structures",
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column("title", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("pattern_id", sa.UUID(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ["pattern_id"], ["patterns.id"], name="pile_structures_pattern_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="pile_structures_pkey"),
    )
    op.create_table(
        "carpets",
        sa.Column("id", sa.UUID(), autoincrement=False, nullable=False),
        sa.Column("title", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("width", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("height", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("price", sa.NUMERIC(), autoincrement=False, nullable=True),
        sa.Column("retail_price", sa.NUMERIC(), autoincrement=False, nullable=True),
        sa.Column("pattern_id", sa.UUID(), autoincrement=False, nullable=True),
        sa.Column(
            "image_paths",
            postgresql.ARRAY(sa.VARCHAR()),
            autoincrement=False,
            nullable=True,
        ),
        sa.Column("stock_amount", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(
            ["pattern_id"], ["patterns.id"], name="carpets_pattern_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="carpets_pkey"),
    )
