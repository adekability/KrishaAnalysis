"""second migration

Revision ID: d54d1a2d974b
Revises: fe9ed9b473c2
Create Date: 2023-04-22 17:53:24.424332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd54d1a2d974b'
down_revision = 'fe9ed9b473c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parameters', schema=None) as batch_op:
        batch_op.add_column(sa.Column('street', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('house_num', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('date', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('parameters', schema=None) as batch_op:
        batch_op.drop_column('date')
        batch_op.drop_column('house_num')
        batch_op.drop_column('street')

    # ### end Alembic commands ###
