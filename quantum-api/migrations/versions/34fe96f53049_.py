"""empty message

Revision ID: 34fe96f53049
Revises: 43f3fe0f1fa1
Create Date: 2020-04-17 16:16:04.494204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34fe96f53049'
down_revision = '43f3fe0f1fa1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('student_id', table_name='circuits')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('student_id', 'circuits', ['student_id'], unique=True)
    # ### end Alembic commands ###
