"""empty message

Revision ID: 4aabc2928032
Revises: e68a4bbda5e1
Create Date: 2022-07-25 09:53:56.586279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4aabc2928032'
down_revision = 'e68a4bbda5e1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('GroupMember', sa.Column('member_id', sa.BigInteger(), nullable=False))
    op.drop_column('GroupMember', 'phase_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('GroupMember', sa.Column('phase_id', sa.BIGINT(), autoincrement=False, nullable=False))
    op.drop_column('GroupMember', 'member_id')
    # ### end Alembic commands ###
