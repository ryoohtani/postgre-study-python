from models.connector_db import DbConnecotor
from models.create_db import DbCreate
from models.insert_db import DbInsert
from models.select_db import DbSelect

basic_data = DbConnecotor(
    user = "admin",
    password = "pypost",
    host = "172.21.0.2",
    port = "5432",
    dbname = "test_database")

# pypost_connectでDB接続とカーソル作成
basic_data.pypost_connect()

# テーブルの作成
db_creator = DbCreate(basic_data)
db_creator.learning_table()
db_creator.subid_table()

# テーブルへinsert
db_insert = DbInsert(basic_data)
db_insert.insert_data()
db_insert.insert_subdata()

# テーブルの抽出
db_select = DbSelect(basic_data)
db_select.select_data()
db_select.select_data2()
db_select.select_data_join()