import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

dburl=config.db_url


#sqlalchemy setup
engine =create_engine(dburl, future=True)
session_local= sessionmaker(bind=engine, expire_on_commit=False,autoflush=False,autocommit=False)


class Base(DeclarativeBase):
    pass

def init_db():
    from orm_models import *
    Base.metadata.create_all(bind=engine)