import datetime as dt
import sqlalchemy as sa
from pypiorg.data.db_session import SqlAlchemyBase


class ProgrammingLanguage(SqlAlchemyBase):
    __tablename__ = 'languages'

    id = sa.Column(sa.String, primary_key=True)
    created_date = sa.Column(sa.DateTime, default=dt.datetime.now, index=True)
    description = sa.Column(sa.String)
