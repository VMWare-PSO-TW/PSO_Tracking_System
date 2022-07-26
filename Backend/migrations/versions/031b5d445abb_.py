"""empty message

Revision ID: 031b5d445abb
Revises: d83fb9feaf19
Create Date: 2022-07-22 21:48:04.790059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '031b5d445abb'
down_revision = 'd83fb9feaf19'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Group',
    sa.Column('group_id', sa.BigInteger(), nullable=False),
    sa.Column('phase_id', sa.BigInteger(), nullable=False),
    sa.Column('internal_hours', sa.BigInteger(), nullable=True),
    sa.Column('subb_hours', sa.BigInteger(), nullable=True),
    sa.PrimaryKeyConstraint('group_id')
    )
    op.create_table('Member',
    sa.Column('member_id', sa.BigInteger(), nullable=False),
    sa.Column('first_name', sa.String(length=20), nullable=False),
    sa.Column('last_name', sa.String(length=20), nullable=False),
    sa.Column('role', sa.String(length=30), nullable=False),
    sa.Column('employee', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('member_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Member')
    op.drop_table('Group')
    # ### end Alembic commands ###
