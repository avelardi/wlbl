"""
api/lib/db.py
Created by Anthony Velardi on 01-19-2017

Core db functions for fun and profit
"""

from api.lib.aux import getsecret, getconfig
import sqlalchemy
from sqlalchemy.orm.session import sessionmaker
from api.lib.models import Base

def db_info(ref='main'):
  """This function handles determining the db type and load the params.
  It should return a standardized string that sqlalchemy can use"""
  c = getsecret()
  if c[ref]['db']['type'] == 'sqlite':
    return c[ref]['db']['sock'], c[ref]['db']['echo']
  if c[ref]['db']['type'] == 'ram':
    return "sqlite:///:memory:", c[ref]['db']['echo']
  else:
    return None
    #unsupported db type returns None
    #TODO: return better errorsz

def get_db(ref='main'):
  db,echobool = db_info()
  if db:
    return sqlalchemy.create_engine(db,echo=echobool)
  else:
    return "Shits broke"

def make_tables(base=Base):
  e = get_db()
  base.metadata.create_all(e)

def get_db_session():
  engine = get_db()
  Base.metadata.bind = engine
  dbsession = sessionmaker(bind=engine)
  return dbsession()
