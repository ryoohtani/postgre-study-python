import sqlalchemy

from setting import engine
from setting import base

class DbTbl(base):
    __tablename__ = "learning_table"

    EMPLOYEE_CODE = sqlalchemy.Column("EMPLOYEE_CODE", sqlalchemy.VARCHAR(10), primary_key = True, nullable = False)
    POSITION_NO = sqlalchemy.Column("POSITION_NO", sqlalchemy.VARCHAR(5), nullable = False, autoincrement = True)
    GENDER = sqlalchemy.Column("GENDER", sqlalchemy.VARCHAR(1))
    BASE_SALARY = sqlalchemy.Column("BASE_SALARY", sqlalchemy.Integer)
    DATE_OF_HIRE = sqlalchemy.Column("DATE_OF_HIRE", sqlalchemy.Date)
# DbTblに定義している情報を元にテーブル作成
base.metadata.create_all(engine)

class DbTbl2(base):
    __tablename__ = "subid_table"

    EMPLOYEE_CODE = sqlalchemy.Column("EMPLOYEE_CODE", sqlalchemy.VARCHAR(10), primary_key = True, nullable = False)
    EMPLOYEE_NAME = sqlalchemy.Column("EMPLOYEE_NAME", sqlalchemy.VARCHAR(20), nullable = False)
    COUNTRY = sqlalchemy.Column("COUNTRY", sqlalchemy.VARCHAR(20), nullable = False)
    COUNTRY_NO = sqlalchemy.Column("COUNTRY_NO", sqlalchemy.Integer)
    ENROLLMENT_ID = sqlalchemy.Column("ENROLLMENT_ID", sqlalchemy.Integer)
# DbTbl2に定義している情報を元にテーブル作成
base.metadata.create_all(engine)