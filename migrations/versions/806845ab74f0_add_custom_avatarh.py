"""Add custom avatarh

Revision ID: 806845ab74f0
Revises: 212b6aa5ae84
Create Date: 2017-09-05 11:00:23.238366

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '806845ab74f0'
down_revision = '212b6aa5ae84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('avatar', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'avatar')
    # ### end Alembic commands ###
