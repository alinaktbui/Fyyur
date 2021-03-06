"""empty message

Revision ID: 0218a9383666
Revises: dd3360d9f060
Create Date: 2020-01-29 21:06:44.564375

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0218a9383666'
down_revision = 'dd3360d9f060'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue', sa.String(length=120), nullable=True))
    op.alter_column('Artist', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
    op.drop_constraint('Artist_venue_id_fkey', 'Artist', type_='foreignkey')
    op.drop_column('Artist', 'venue_id')
    op.add_column('Shows', sa.Column('Artist_id', sa.Integer(), nullable=False))
    op.add_column('Shows', sa.Column('Venue_id', sa.Integer(), nullable=False))
    op.drop_constraint('artistfk', 'Shows', type_='foreignkey')
    op.drop_constraint('Shows_venue_id_fkey', 'Shows', type_='foreignkey')
    op.create_foreign_key(None, 'Shows', 'Venue', ['Venue_id'], ['id'])
    op.create_foreign_key(None, 'Shows', 'Artist', ['Artist_id'], ['id'])
    op.drop_column('Shows', 'venue_id')
    op.drop_column('Shows', 'artist_id')
    op.add_column('Venue', sa.Column('genres', sa.ARRAY(sa.String(length=120)), nullable=True))
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('website', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'website')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'genres')
    op.add_column('Shows', sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('Shows', sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'Shows', type_='foreignkey')
    op.drop_constraint(None, 'Shows', type_='foreignkey')
    op.create_foreign_key('Shows_venue_id_fkey', 'Shows', 'Venue', ['venue_id'], ['id'])
    op.create_foreign_key('artistfk', 'Shows', 'Artist', ['artist_id'], ['id'])
    op.drop_column('Shows', 'Venue_id')
    op.drop_column('Shows', 'Artist_id')
    op.add_column('Artist', sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('Artist_venue_id_fkey', 'Artist', 'Venue', ['venue_id'], ['id'])
    op.alter_column('Artist', 'genres',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'seeking_description')
    # ### end Alembic commands ###
