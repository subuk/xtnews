
import datetime
import dateutil.tz

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

def now():
    return datetime.datetime.now(dateutil.tz.tzutc())

class News(Base):
    __tablename__ = 'news'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.Text)
    text = sa.Column(sa.Text)
    date_created = sa.Column(sa.DateTime(), default=now)

    def __init__(self, title=None, text=None):
        self.title = title
        self.text = text

    def as_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'date_created': self.date_created,
        }
