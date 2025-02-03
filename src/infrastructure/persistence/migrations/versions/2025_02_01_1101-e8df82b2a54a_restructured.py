"""restructured

Revision ID: e8df82b2a54a
Revises: d12c4ea5f70b
Create Date: 2025-02-01 11:01:56.630750

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'e8df82b2a54a'
down_revision: Union[str, None] = 'd12c4ea5f70b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('carpets', sa.Column('image_paths', postgresql.ARRAY(sa.String()), nullable=True))
    op.add_column('carpets', sa.Column('pattern_id', sa.UUID(), nullable=True))
    op.create_foreign_key(None, 'carpets', 'patterns', ['pattern_id'], ['id'])
    op.drop_column('patterns', 'image_paths')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patterns', sa.Column('image_paths', postgresql.ARRAY(sa.VARCHAR()), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'carpets', type_='foreignkey')
    op.drop_column('carpets', 'pattern_id')
    op.drop_column('carpets', 'image_paths')
    # ### end Alembic commands ###
