# file location of the sqlite db
from os import path

class Config:

    def __init__(self):
        self.sqlite_uri = 'sqlite:///' + path.abspath(path.join(path.dirname(__file__), '..', 'storage.sqlite'))

config = Config()
