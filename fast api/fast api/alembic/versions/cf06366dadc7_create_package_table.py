"""create package table

Revision ID: cf06366dadc7
Revises: 8446bcb7a5fa
Create Date: 2021-09-08 14:34:35.486249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf06366dadc7'
down_revision = '8446bcb7a5fa'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'package',
        sa.Column('type', sa.String(1), primary_key=True),
        sa.Column('description', sa.String(150)),
    )

def downgrade():
    op.drop_table('package')