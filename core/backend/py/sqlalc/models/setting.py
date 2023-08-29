import sqlalchemy
import sqlalchemy.orm

DATABASE_URL = "postgresql://admin:pypost@172.21.0.2/test_database"

engine = sqlalchemy.create_engine(DATABASE_URL, echo = True)
# ORM(オブジェクトとRDB内のテーブルやレコードとの間でデータの変換や操作を自動的に行う)
base = sqlalchemy.orm.declarative_base()
# DBのテーブルからデータを取得するためにセッションを作成
session = sqlalchemy.orm.sessionmaker(bind = engine)