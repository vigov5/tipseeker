"""Added link table

Revision ID: 2d89b4228948
Revises: 
Create Date: 2020-10-10 17:15:28.730393

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2d89b4228948'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('links', sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('title', sa.String(length=500), nullable=True),
                    sa.Column('url', sa.String(length=500), nullable=True),
                    sa.Column('media', sa.String(length=500), nullable=True),
                    sa.Column('origin', sa.String(length=500), nullable=False),
                    sa.Column('content', sa.Text(), nullable=True),
                    sa.Column('read', sa.SmallInteger(), nullable=False),
                    sa.Column('kind', sa.SmallInteger(), nullable=False),
                    sa.Column('category', sa.SmallInteger(), nullable=False),
                    sa.Column('status', sa.SmallInteger(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.PrimaryKeyConstraint('id'))
    op.create_index('url', 'links', ['url'])


def downgrade():
    op.drop_table('links')
