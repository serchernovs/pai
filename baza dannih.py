from sqlalchemy import create_engine
from sqlalchemy.engine import base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker

database_name = 'programisti'

engine = create_engine(f'programisti:///{database_name}')
session = sessionmaker(bind=engine)

base = declarative_base()

def create_db():
    base.metadata.create_all(engine)