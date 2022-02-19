"""books table add field

Revision ID: bd50a7800186
Revises: 6262a714f9f2
Create Date: 2022-02-18 18:33:53.199287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd50a7800186'
down_revision = '6262a714f9f2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('purchased', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'purchased')
    # ### end Alembic commands ###