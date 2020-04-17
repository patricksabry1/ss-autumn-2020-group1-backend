"""empty message

Revision ID: c031ff41e477
Revises: fa99a81d5808
Create Date: 2020-04-17 16:01:09.457710

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c031ff41e477'
down_revision = 'fa99a81d5808'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=191), nullable=False),
    sa.Column('last_name', sa.String(length=191), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('student_id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('circuits',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('circuit_name', sa.String(length=191), nullable=False),
    sa.Column('circuit_json', sa.Text(length=4294000000), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['users.student_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('circuits')
    op.drop_table('users')
    # ### end Alembic commands ###
