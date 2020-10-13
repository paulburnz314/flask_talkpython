import datetime as dt
from typing import List
import sqlalchemy as sa
import sqlalchemy.orm as orm
from pypiorg.data.db_session import SqlAlchemyBase
from pypiorg.data.releases import Release


class Package(SqlAlchemyBase):
	__tablename__ = 'packages'

	id = sa.Column(sa.String, primary_key=True)
	created_date = sa.Column(sa.DateTime, default=dt.datetime.now, index=True)
	summary = sa.Column(sa.String(200), nullable=False)
	description = sa.Column(sa.String(200), nullable=True)
	home_page = sa.Column(sa.String)
	docs_url = sa.Column(sa.String)
	package_url = sa.Column(sa.String)

	author_name = sa.Column(sa.String)
	author_email = sa.Column(sa.String, index=True)

	license = sa.Column(sa.String, index=True)
	# releases relationship
	# releases = sa.relationship("Release", backref='Pypackage', lazy='dynamic')
	releases: List[Release] = orm.relation("Release", order_by=[
		Release.major_ver.desc(),
		Release.minor_ver.desc(),
		Release.build_ver.desc(),
	], back_populates='package')

	# maintainers and releases

	def __repr__(self):
		return f'<Package {self.id}>'
