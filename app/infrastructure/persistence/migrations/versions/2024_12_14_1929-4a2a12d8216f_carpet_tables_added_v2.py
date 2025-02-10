"""carpet tables added v2

Revision ID: 4a2a12d8216f
Revises: bc0fadc4679a
Create Date: 2024-12-14 19:29:11.109229

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = "4a2a12d8216f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "colors",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "pile_structures",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "patterns",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("pile_structure", sa.UUID(), nullable=True),
        sa.Column("color", sa.UUID(), nullable=True),
        sa.ForeignKeyConstraint(
            ["color"],
            ["colors.id"],
        ),
        sa.ForeignKeyConstraint(
            ["pile_structure"],
            ["pile_structures.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "carpets",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("width", sa.String(), nullable=True),
        sa.Column("height", sa.String(), nullable=True),
        sa.Column("price", sa.Numeric(), nullable=True),
        sa.Column("retail_price", sa.Numeric(), nullable=True),
        sa.Column("pattern_id", sa.UUID(), nullable=True),
        sa.Column("image_paths", postgresql.ARRAY(sa.String()), nullable=True),
        sa.Column("stock_amount", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["pattern_id"],
            ["patterns.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("carpets")
    op.drop_table("patterns")
    op.drop_table("pile_structures")
    op.drop_table("colors")
