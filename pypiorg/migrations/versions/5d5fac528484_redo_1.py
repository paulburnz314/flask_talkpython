"""redo 1

Revision ID: 5d5fac528484
Revises: 
Create Date: 2020-09-29 13:35:47.881857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d5fac528484'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('downloads',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('package_id', sa.String(), nullable=True),
    sa.Column('release_id', sa.BigInteger(), nullable=True),
    sa.Column('ip_address', sa.String(), nullable=True),
    sa.Column('user_agent', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_downloads_created_date'), 'downloads', ['created_date'], unique=False)
    op.create_index(op.f('ix_downloads_package_id'), 'downloads', ['package_id'], unique=False)
    op.create_index(op.f('ix_downloads_release_id'), 'downloads', ['release_id'], unique=False)
    op.create_table('languages',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_languages_created_date'), 'languages', ['created_date'], unique=False)
    op.create_table('licenses',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_licenses_created_date'), 'licenses', ['created_date'], unique=False)
    op.create_table('maintainers',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('package_id', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('user_id', 'package_id')
    )
    op.create_table('packages',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('summary', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('home_page', sa.String(), nullable=True),
    sa.Column('docs_url', sa.String(), nullable=True),
    sa.Column('package_url', sa.String(), nullable=True),
    sa.Column('author_name', sa.String(), nullable=True),
    sa.Column('author_email', sa.String(), nullable=True),
    sa.Column('license', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_packages_author_email'), 'packages', ['author_email'], unique=False)
    op.create_index(op.f('ix_packages_created_date'), 'packages', ['created_date'], unique=False)
    op.create_index(op.f('ix_packages_license'), 'packages', ['license'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('profile_image_url', sa.String(), nullable=True),
    sa.Column('last_login', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_created_date'), 'users', ['created_date'], unique=False)
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_hashed_password'), 'users', ['hashed_password'], unique=False)
    op.create_index(op.f('ix_users_last_login'), 'users', ['last_login'], unique=False)
    op.create_table('releases',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('package_id', sa.String(), nullable=True),
    sa.Column('major_ver', sa.BigInteger(), nullable=True),
    sa.Column('minor_ver', sa.BigInteger(), nullable=True),
    sa.Column('build_ver', sa.BigInteger(), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('size', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['package_id'], ['packages.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_releases_build_ver'), 'releases', ['build_ver'], unique=False)
    op.create_index(op.f('ix_releases_created_date'), 'releases', ['created_date'], unique=False)
    op.create_index(op.f('ix_releases_major_ver'), 'releases', ['major_ver'], unique=False)
    op.create_index(op.f('ix_releases_minor_ver'), 'releases', ['minor_ver'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_releases_minor_ver'), table_name='releases')
    op.drop_index(op.f('ix_releases_major_ver'), table_name='releases')
    op.drop_index(op.f('ix_releases_created_date'), table_name='releases')
    op.drop_index(op.f('ix_releases_build_ver'), table_name='releases')
    op.drop_table('releases')
    op.drop_index(op.f('ix_users_last_login'), table_name='users')
    op.drop_index(op.f('ix_users_hashed_password'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_index(op.f('ix_users_created_date'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_packages_license'), table_name='packages')
    op.drop_index(op.f('ix_packages_created_date'), table_name='packages')
    op.drop_index(op.f('ix_packages_author_email'), table_name='packages')
    op.drop_table('packages')
    op.drop_table('maintainers')
    op.drop_index(op.f('ix_licenses_created_date'), table_name='licenses')
    op.drop_table('licenses')
    op.drop_index(op.f('ix_languages_created_date'), table_name='languages')
    op.drop_table('languages')
    op.drop_index(op.f('ix_downloads_release_id'), table_name='downloads')
    op.drop_index(op.f('ix_downloads_package_id'), table_name='downloads')
    op.drop_index(op.f('ix_downloads_created_date'), table_name='downloads')
    op.drop_table('downloads')
    # ### end Alembic commands ###