"""add content column to posts table

Revision ID: f31c1c68eccd
Revises: a3b489ff2520
Create Date: 2021-11-08 16:17:05.129472

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f31c1c68eccd'
down_revision = 'a3b489ff2520'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('post',sa.Column('content', sa.String(), nullable=False))


def downgrade():
    op.drop_column('post','content')
