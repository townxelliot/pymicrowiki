from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Page(Base):
    __tablename__ = 'page'

    id = Column(Integer, primary_key=True)
    content = Column(String)

    def __repr__(self):
      return f'<Page(id={self.id})>'
