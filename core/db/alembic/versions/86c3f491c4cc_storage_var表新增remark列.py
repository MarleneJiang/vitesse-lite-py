"""storage_var表新增remark列

Revision ID: 86c3f491c4cc
Revises: f315a762b0fe
Create Date: 2023-03-14 22:44:57.982689

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86c3f491c4cc'
down_revision = 'f315a762b0fe'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('storage_var', sa.Column('remark', sa.String(), server_default='', nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('storage_var', 'remark')
    # ### end Alembic commands ###
