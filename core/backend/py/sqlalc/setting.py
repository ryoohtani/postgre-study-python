import sqlalchemy
import sqlalchemy.orm


DATABASE_URL = "postgresql://admin:pypost@172.21.0.2/test_database"

engine = sqlalchemy.create_engine(DATABASE_URL, echo = True)

base = sqlalchemy.orm.declarative_base()

session = sqlalchemy.orm.sessionmaker(bind = engine)