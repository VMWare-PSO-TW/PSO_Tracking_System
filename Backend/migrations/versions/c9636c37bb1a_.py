"""empty message

Revision ID: c9636c37bb1a
Revises: 031b5d445abb
Create Date: 2022-07-25 09:12:06.496526

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9636c37bb1a'
down_revision = '031b5d445abb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Engagement', sa.Column('start_date', sa.DateTime(), nullable=True))
    op.add_column('Engagement', sa.Column('end_date', sa.DateTime(), nullable=True))
    op.add_column('Phase', sa.Column('start_date', sa.DateTime(), nullable=True))
    op.add_column('Phase', sa.Column('end_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Phase', 'end_date')
    op.drop_column('Phase', 'start_date')
    op.drop_column('Engagement', 'end_date')
    op.drop_column('Engagement', 'start_date')
    # ### end Alembic commands ###
