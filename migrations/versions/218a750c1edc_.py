"""empty message

Revision ID: 218a750c1edc
Revises: 808febc65eeb
Create Date: 2020-02-26 20:17:57.164134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '218a750c1edc'
down_revision = '808febc65eeb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('password', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'password')
    # ### end Alembic commands ###
