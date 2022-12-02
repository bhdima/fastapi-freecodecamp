"""add foreign-key to posts table

Revision ID: 114ce2dfc61b
Revises: 0b6b7273b481
Create Date: 2022-12-01 20:17:08.732463

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '114ce2dfc61b'
down_revision = '0b6b7273b481'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass