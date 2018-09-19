"""task table

Revision ID: 5b8f36d8470d
Revises: 
Create Date: 2018-09-19 09:40:24.155604

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b8f36d8470d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('result_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('answer', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('results',
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
    op.drop_table('results')
    op.drop_table('result_table')
    # ### end Alembic commands ###