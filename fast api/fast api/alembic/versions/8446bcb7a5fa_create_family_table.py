"""create family table

Revision ID: 8446bcb7a5fa
Revises: 6a122a911429
Create Date: 2021-09-08 14:18:33.563197

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8446bcb7a5fa'
down_revision = '6a122a911429'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'family',
        sa.Column('family_id', sa.Integer, primary_key=True),
        sa.Column('member_count', sa.String(50)),
    )

def downgrade():
    op.drop_table('family')