import sqlalchemy

from setting import engine
from setting import base

class DbTbl(base):
    __tablename__ = "learning_table"
