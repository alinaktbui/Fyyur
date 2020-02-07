"""empty message

Revision ID: 6e34fa7198c1
Revises: c724a0ce656b
Create Date: 2020-02-03 21:39:48.473860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e34fa7198c1'
down_revision = 'c724a0ce656b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Artist', 'seeking_description',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    op.alter_column('Artist', 'seeking_venue',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.add_column('Shows', sa.Column('artist_id', sa.Integer(), nullable=True))
    op.add_column('Shows', sa.Column('venue_id', sa.Integer(), nullable=True))
    op.drop_constraint('Shows_Venue_id_fkey', 'Shows', type_='foreignkey')
    op.drop_constraint('Shows_Artist_id_fkey', 'Shows', type_='foreignkey')
    op.create_foreign_key(None, 'Shows', 'Venue', ['venue_id'], ['id'])
    op.create_foreign_key(None, 'Shows', 'Artist', ['artist_id'], ['id'])
    op.drop_column('Shows', 'Venue_id')
    op.drop_column('Shows', 'Artist_id')
    op.drop_column('Shows', 'id')
    op.alter_column('Venue', 'seeking_description',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Venue', 'seeking_description',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    op.add_column('Shows', sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('Shows', sa.Column('Artist_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('Shows', sa.Column('Venue_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'Shows', type_='foreignkey')
    op.drop_constraint(None, 'Shows', type_='foreignkey')
    op.create_foreign_key('Shows_Artist_id_fkey', 'Shows', 'Artist', ['Artist_id'], ['id'])
    op.create_foreign_key('Shows_Venue_id_fkey', 'Shows', 'Venue', ['Venue_id'], ['id'])
    op.drop_column('Shows', 'venue_id')
    op.drop_column('Shows', 'artist_id')
    op.alter_column('Artist', 'seeking_venue',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.alter_column('Artist', 'seeking_description',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    # ### end Alembic commands ###
