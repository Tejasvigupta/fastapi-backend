"""create posts table

Revision ID: a3b489ff2520
Revises: 
Create Date: 2021-11-08 15:36:39.155377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3b489ff2520'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('post',sa.Column('id',sa.Integer(), nullable=False,primary_key=True),
    sa.Column('title',sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('post')
    pass
