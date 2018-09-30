"""empty message

Revision ID: 107766b892a5
Revises: 0002a859d965
Create Date: 2018-09-29 21:37:39.343600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '107766b892a5'
down_revision = '0002a859d965'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feedbacks_ver_easy')
    op.drop_table('feedbacks_ver_game')
    op.add_column('feedbacks', sa.Column('version', sa.Text(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('feedbacks', 'version')
    op.create_table('feedbacks_ver_game',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('userid', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('feedback', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('duration', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='feedbacks_ver_game_pkey')
    )
    op.create_table('feedbacks_ver_easy',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('userid', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('feedback', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('duration', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='feedbacks_ver_easy_pkey')
    )
    # ### end Alembic commands ###