"""new tables structure

Revision ID: f8620ac80deb
Revises: 942aa98fe4ec
Create Date: 2024-12-25 09:10:33.875008

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = "f8620ac80deb"
down_revision: Union[str, None] = "942aa98fe4ec"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "carpets",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=True),
        sa.Column("last_name", sa.String(), nullable=True),
        sa.Column("email", sa.String(), nullable=True),
        sa.Column("telegram_username", sa.String(), nullable=True),
        sa.Column("telegram_id", sa.String(), nullable=True),
        sa.Column("phone_number", sa.String(), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "users",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("color", sa.String(), nullable=True),
        sa.Column("width", sa.Integer(), nullable=True),
        sa.Column("height", sa.Integer(), nullable=True),
        sa.Column("base_price", sa.Numeric(precision=10, scale=2), nullable=True),
        sa.Column("retail_price", sa.Numeric(precision=10, scale=2), nullable=True),
        sa.Column("stock_amount", sa.Integer(), nullable=True),
        sa.Column("pile_structure", sa.String(), nullable=True),
        sa.Column("main_image_path", sa.String(), nullable=True),
        sa.Column("image_paths", postgresql.ARRAY(sa.String()), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("users")
    op.drop_table("carpets")
