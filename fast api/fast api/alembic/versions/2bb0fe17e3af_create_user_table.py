"""create user table

Revision ID: 2bb0fe17e3af
Revises: cf06366dadc7
Create Date: 2021-09-08 14:37:46.806907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bb0fe17e3af'
down_revision = 'cf06366dadc7'
branch_labels = None
depends_on = None



def upgrade():
    op.create_table(
        'user',
        sa.Column("username", sa.String(30), primary_key=True, unique=True),
        sa.Column("password", sa.String(100), nullable=False),
        sa.Column("lastname",  sa.String(30), nullable=False),
        sa.Column("firstname", sa.String(30), nullable=False),
        sa.Column("phone_number", sa.String(16)),
        sa.Column("gender", sa.String(5), nullable=False),
        sa.Column("pg",sa.String(1),  sa.ForeignKey("package.type", ondelete="SET NULL")),
        sa.Column("parent_of", sa.Integer,  sa.ForeignKey("family.family_id", ondelete="SET NULL")),
        sa.Column("child_of", sa.Integer,  sa.ForeignKey("family.family_id", ondelete="SET NULL"))
    )


def downgrade():
    op.drop_table('user')