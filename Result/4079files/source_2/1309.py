"""Use a new table for UIDs

Revision ID: 56e1574fe7b
Revises: 2e82d01dc7d
Create Date: 2015-08-24 11:30:42.750224

"""

# revision identifiers, used by Alembic.
revision = '56e1574fe7b'
down_revision = '2e82d01dc7d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('UID',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('full_uid', sa.String(), nullable=True),
                    sa.Column('uid_name', sa.String(), nullable=True),
                    sa.Column('uid_email', sa.String(), nullable=True),
                    sa.Column('uid_comment', sa.String(), nullable=True),
                    sa.Column('key_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['key_id'], ['key.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.drop_column('key', 'uid')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('key', sa.Column('uid', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_table('UID')
    ### end Alembic commands ###
