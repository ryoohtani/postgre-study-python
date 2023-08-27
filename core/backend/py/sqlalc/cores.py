# import psycopg2
import sqlalchemy
import sqlalchemy.orm

DATABASE_URL = "postgresql://admin:pypost@172.21.0.2/test_database"

engine = sqlalchemy.create_engine(DATABASE_URL)

# ORM(オブジェクトとRDB内のテーブルやレコードとの間でデータの変換や操作を自動的に行う)
base = sqlalchemy.orm.declarative_base()

# DBのテーブルからデータを取得するためにセッションを作成
session = sqlalchemy.orm.sessionmaker(bind = engine)
ses = session()

class DbConnecotor(base):
    __tablename__ = "learning_table"

    EMPLOYEE_CODE = sqlalchemy.Column(sqlalchemy.VARCHAR(10), primary_key = True, nullable = False)
    POSITION_NO = sqlalchemy.Column(sqlalchemy.VARCHAR(5), nullable = False)
    GENDER = sqlalchemy.Column(sqlalchemy.VARCHAR(1))
    BASE_SALARY = sqlalchemy.Column(sqlalchemy.Integer)
    DATE_OF_HIRE = sqlalchemy.Column(sqlalchemy.Date)

# DbConnecotorに定義している情報を元にテーブル作成
base.metadata.create_all(engine)