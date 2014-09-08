"""empty message

Revision ID: 15f93ea5fd51
Revises: 4e1d3fc4370b
Create Date: 2014-09-08 06:38:28.600000

"""

# revision identifiers, used by Alembic.
revision = '15f93ea5fd51'
down_revision = '4e1d3fc4370b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('results_id', sa.Integer(), nullable=True),
    sa.Column('white_id', sa.Integer(), nullable=True),
    sa.Column('black_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['black_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['results_id'], ['result.id'], ),
    sa.ForeignKeyConstraint(['white_id'], ['user.id'], )
    )
    op.drop_column(u'result', 'white_id')
    op.drop_column(u'result', 'black_id')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'result', sa.Column('black_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column(u'result', sa.Column('white_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_table('games')
    ### end Alembic commands ###