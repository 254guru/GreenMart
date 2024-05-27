"""Initial migration

Revision ID: ad9b254539ab
Revises: 
Create Date: 2024-05-25 23:13:55.548167

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad9b254539ab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_column('status')

    with op.batch_alter_table('order_item', schema=None) as batch_op:
        batch_op.drop_column('subtotal')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('order_item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('subtotal', sa.FLOAT(), nullable=False))

    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.VARCHAR(length=20), nullable=True))

    # ### end Alembic commands ###