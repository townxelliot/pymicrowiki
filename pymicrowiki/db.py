from flask import g

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from pymicrowiki import config


class Db:

    def __init__(self, sqlite_uri):
        engine = create_engine(sqlite_uri, echo=True, connect_args={'check_same_thread': False})
        self.sessionClass = sessionmaker(bind=engine)

    def query(self, *args, **kwargs):
        session = self.sessionClass()
        return session.query(*args, **kwargs)

    def add(self, obj):
        session = self.sessionClass()
        session.add(obj)
        return session.commit()

    def delete(self, modelClass, id):
        session = self.sessionClass()
        obj = session.query(modelClass).filter(modelClass.id==id).first()
        session.delete(obj)
        return session.commit()


def get_db():
    if 'db' not in g:
        g.db = Db(config.sqlite_uri)
    return g.db
