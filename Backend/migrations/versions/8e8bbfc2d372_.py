"""empty message

Revision ID: 8e8bbfc2d372
Revises: c0d6edc78787
Create Date: 2022-09-01 11:33:27.303539

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8e8bbfc2d372'
down_revision = 'c0d6edc78787'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Engagement', sa.Column('budgeted_hours', sa.BigInteger(), nullable=True))
    op.add_column('Engagement', sa.Column('finish_date', sa.DateTime(), nullable=True))
    op.add_column('Engagement', sa.Column('last_entry_date', sa.DateTime(), nullable=True))
    op.add_column('Engagement', sa.Column('hours_balance', sa.BigInteger(), nullable=True))
    op.add_column('Engagement', sa.Column('inactive_days', sa.BigInteger(), nullable=True))
    op.alter_column('Engagement', 'expect_hours',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.alter_column('Engagement', 'actual_hours',
               existing_type=sa.BIGINT(),
               nullable=True)
    op.drop_column('Engagement', 'internal_hours')
    op.drop_column('Engagement', 'end_date')
    op.drop_column('Engagement', 'subb_hours')
    op.add_column('GroupMember', sa.Column('engagement_id', sa.String(length=30), nullable=True))
    op.add_column('GroupMember', sa.Column('phase_name', sa.Text(), nullable=True))
    op.alter_column('Phase', 'name',
               existing_type=sa.VARCHAR(length=200),
               type_=sa.String(length=500),
               existing_nullable=False)
    op.drop_column('Phase', 'end_date')
    op.drop_column('Phase', 'start_date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Phase', sa.Column('start_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('Phase', sa.Column('end_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.alter_column('Phase', 'name',
               existing_type=sa.String(length=500),
               type_=sa.VARCHAR(length=200),
               existing_nullable=False)
    op.drop_column('GroupMember', 'phase_name')
    op.drop_column('GroupMember', 'engagement_id')
    op.add_column('Engagement', sa.Column('subb_hours', sa.BIGINT(), autoincrement=False, nullable=True))
    op.add_column('Engagement', sa.Column('end_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('Engagement', sa.Column('internal_hours', sa.BIGINT(), autoincrement=False, nullable=True))
    op.alter_column('Engagement', 'actual_hours',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('Engagement', 'expect_hours',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.drop_column('Engagement', 'inactive_days')
    op.drop_column('Engagement', 'hours_balance')
    op.drop_column('Engagement', 'last_entry_date')
    op.drop_column('Engagement', 'finish_date')
    op.drop_column('Engagement', 'budgeted_hours')
    # ### end Alembic commands ###
