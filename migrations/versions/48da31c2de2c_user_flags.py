"""user flags

Revision ID: 48da31c2de2c
Revises: 43c24fc4dd24
Create Date: 2019-08-19 16:38:18.529600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48da31c2de2c'
down_revision = '43c24fc4dd24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('read_toc', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('wants_credit', sa.Boolean(), nullable=True))
    op.add_column('user', sa.Column('wants_updates', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'wants_updates')
    op.drop_column('user', 'wants_credit')
    op.drop_column('user', 'read_toc')
    # ### end Alembic commands ###
