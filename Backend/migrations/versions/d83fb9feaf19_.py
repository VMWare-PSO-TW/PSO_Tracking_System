"""empty message

Revision ID: d83fb9feaf19
Revises: 92960c651ae2
Create Date: 2022-07-22 21:47:41.008294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd83fb9feaf19'
down_revision = '92960c651ae2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Member')
    op.drop_table('Group')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Group',
    sa.Column('group_id', sa.BIGINT(), server_default=sa.text('nextval(\'"Group_group_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('phase_id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('internal_hours', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('subb_hours', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('group_id', name='Group_pkey')
    )
    op.create_table('Member',
    sa.Column('member_id', sa.BIGINT(), server_default=sa.text('nextval(\'"Member_member_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('role', sa.VARCHAR(length=30), autoincrement=False, nullable=False),
    sa.Column('employee', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('member_id', name='Member_pkey')
    )
    # ### end Alembic commands ###
