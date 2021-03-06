"""empty message

Revision ID: 0002a859d965
Revises: 900ef7f87e6d
Create Date: 2018-09-29 19:48:57.863652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0002a859d965'
down_revision = '900ef7f87e6d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feedbacks_ver_easy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Text(), nullable=False),
    sa.Column('feedback', sa.Text(), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('results_ver_easy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userid', sa.Text(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('mp3url', sa.Text(), nullable=False),
    sa.Column('queryname', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('results_ver_easy')
    op.drop_table('feedbacks_ver_easy')
    # ### end Alembic commands ###
