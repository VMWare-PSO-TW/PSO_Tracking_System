"""empty message

Revision ID: ee1712bf5c12
Revises: 416890a5e1ca
Create Date: 2022-07-25 09:39:50.786232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ee1712bf5c12'
down_revision = '416890a5e1ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Group', 'phase_id',
               existing_type=sa.BIGINT(),
               type_=sa.String(length=20),
               existing_nullable=False)
    op.alter_column('Phase', 'phase_id',
               existing_type=sa.BIGINT(),
               type_=sa.String(length=20),
               existing_nullable=False,
               existing_server_default=sa.text('nextval(\'"Phase_phase_id_seq"\'::regclass)'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Phase', 'phase_id',
               existing_type=sa.String(length=20),
               type_=sa.BIGINT(),
               existing_nullable=False,
               existing_server_default=sa.text('nextval(\'"Phase_phase_id_seq"\'::regclass)'))
    op.alter_column('Group', 'phase_id',
               existing_type=sa.String(length=20),
               type_=sa.BIGINT(),
               existing_nullable=False)
    # ### end Alembic commands ###
