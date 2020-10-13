import datetime as dt
import sqlalchemy as sa
from pypiorg.data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)
    email = sa.Column(sa.String, index=True, unique=True, nullable=True)
    hashed_password = sa.Column(sa.String, nullable=True, index=True)
    created_date = sa.Column(sa.DateTime, default=dt.datetime.now, index=True)
    profile_image_url = sa.Column(sa.String)
    last_login = sa.Column(sa.DateTime, default=dt.datetime.now, index=True)
