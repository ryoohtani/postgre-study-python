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

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)

# テーブルをデータベースに作成
Base.metadata.create_all(engine)