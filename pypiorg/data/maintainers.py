import sqlalchemy as sa
from pypiorg.data.db_session import SqlAlchemyBase


class Maintainer(SqlAlchemyBase):
    __tablename__ = 'maintainers'

    user_id = sa.Column(sa.Integer, primary_key=True)
    package_id = sa.Column(sa.String, primary_key=True)

