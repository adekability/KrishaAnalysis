"""fourth migration

Revision ID: 1d3ba7546311
Revises: d14dcafc1aab
Create Date: 2023-04-22 18:36:51.104483

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d3ba7546311'
down_revision = 'd14dcafc1aab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parameters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('floor', sa.String(), nullable=True))
        batch_op.drop_column('building_type')
        batch_op.drop_column('count_of_floor')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parameters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('count_of_floor', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('building_type', sa.VARCHAR(), nullable=True))
        batch_op.drop_column('floor')

    # ### end Alembic commands ###