"""carpet tables added v3

Revision ID: 8330a655c2ed
Revises: 4a2a12d8216f
Create Date: 2024-12-15 14:59:05.621702

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "8330a655c2ed"
down_revision: Union[str, None] = "4a2a12d8216f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("colors", sa.Column("pattern_id", sa.UUID(), nullable=True))
    op.create_foreign_key(None, "colors", "patterns", ["pattern_id"], ["id"])
    op.drop_constraint("patterns_color_fkey", "patterns", type_="foreignkey")
    op.drop_constraint("patterns_pile_structure_fkey", "patterns", type_="foreignkey")
    op.drop_column("patterns", "color")
    op.drop_column("patterns", "pile_structure")
    op.add_column("pile_structures", sa.Column("pattern_id", sa.UUID(), nullable=True))
    op.create_foreign_key(None, "pile_structures", "patterns", ["pattern_id"], ["id"])


def downgrade() -> None:
    op.drop_constraint(None, "pile_structures", type_="foreignkey")
    op.drop_column("pile_structures", "pattern_id")
    op.add_column(
        "patterns",
        sa.Column("pile_structure", sa.UUID(), autoincrement=False, nullable=True),
    )
    op.add_column(
        "patterns", sa.Column("color", sa.UUID(), autoincrement=False, nullable=True)
    )
    op.create_foreign_key(
        "patterns_pile_structure_fkey",
        "patterns",
        "pile_structures",
        ["pile_structure"],
        ["id"],
    )
    op.create_foreign_key(
        "patterns_color_fkey", "patterns", "colors", ["color"], ["id"]
    )
    op.drop_constraint(None, "colors", type_="foreignkey")
    op.drop_column("colors", "pattern_id")
