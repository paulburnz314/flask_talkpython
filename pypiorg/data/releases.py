import datetime as dt
import sqlalchemy as sa
import sqlalchemy.orm as orm
from pypiorg.data.db_session import SqlAlchemyBase
# from app import db


class Release(SqlAlchemyBase):
    __tablename__ = 'releases'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    package_id = sa.Column(sa.String, sa.ForeignKey('packages.id'))
    package = orm.relation('Package')
    # SQLite syntax FOREIGN KEY("package_id") REFERENCES "packages"("id")
    major_ver = sa.Column(sa.BigInteger, index=True)
    minor_ver = sa.Column(sa.BigInteger, index=True)
    build_ver = sa.Column(sa.BigInteger, index=True)

    created_date = sa.Column(sa.DateTime, default=dt.datetime.now, index=True)
    comment = sa.Column(sa.String)
    url = sa.Column(sa.String)
    size = sa.Column(sa.BigInteger)

    @property
    def version_text(self):
        return f'{self.major_ver}.{self.minor_ver}.{self.build_ver}'
