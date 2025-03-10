"""restructured v2

Revision ID: 7b5bf0c59be2
Revises: e8df82b2a54a
Create Date: 2025-02-09 17:40:02.941649

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7b5bf0c59be2'
down_revision: Union[str, None] = 'e8df82b2a54a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patterns', sa.Column('region', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patterns', 'region')
    # ### end Alembic commands ###
