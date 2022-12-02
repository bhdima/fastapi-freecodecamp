"""add content column to posts table

Revision ID: ccba4de15231
Revises: fe45d0ae48e7
Create Date: 2022-12-01 20:04:57.669849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccba4de15231'
down_revision = 'fe45d0ae48e7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass