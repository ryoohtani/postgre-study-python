# import psycopg2
import sqlalchemy
import sqlalchemy.orm

DATABASE_URL = "postgresql://admin:pypost@172.21.0.2/test_database"

engine = sqlalchemy.create_engine(DATABASE_URL)

# ORM(オブジェクトとRDB内のテーブルやレコードとの間でデータの変換や操作を自動的に行う)
Base = sqlalchemy.orm.declarative_base()

# セッション
Session = sqlalchemy.orm.sessionmaker(bind = engine)
session = Session()

class DbConnecotor(Base):
    __tablename__ = "learning_table"

    EMPLOYEE_CODE = sqlalchemy.Column(sqlalchemy.VARCHAR(10), primary_key = True, nullable = False)
    POSITION_NO = sqlalchemy.Column(sqlalchemy.VARCHAR(5), nullable = False)
    GENDER = sqlalchemy.Column(sqlalchemy.VARCHAR(1))
    BASE_SALARY = sqlalchemy.Column(sqlalchemy.Integer)
    DATE_OF_HIRE = sqlalchemy.Column(sqlalchemy.Date)

# テーブルをデータベースに作成
Base.metadata.create_all(engine)