"""add new column datetime to game ver

Revision ID: 046aa2f36abf
Revises: 02aab20a3247
Create Date: 2018-10-14 16:57:36.597895

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '046aa2f36abf'
down_revision = '02aab20a3247'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results_ver_game', sa.Column('datetime', sa.Text(), nullable=True))
    op.drop_column('results_ver_game', 'timestamp')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('results_ver_game', sa.Column('timestamp', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('results_ver_game', 'datetime')
    # ### end Alembic commands ###