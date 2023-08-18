from models.connector_db import DbConnecotor
from models.create_db import DbCreate
from models.insert_db import DbInsert

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

# テーブルへinsert
db_insert = DbInsert(basic_data)
db_insert.insert_data()


# # update       
# cursor.execute("""update learning_table set EMPLOYEE_CODE = 's004' where EMPLOYEE_CODE = 's010'""")

# # delete
# cursor.execute("""delete from learning_table where EMPLOYEE_CODE = 's004'""")

# basic_data.commit()

# # Pythonからpostgreへselect
# cursor.execute("""select * from learning_table""")
# datas = cursor.fetchall()
# for data_list in datas:
#     print(data_list)

# cursor.execute("""select * from learning_table where gender = '男'""")
# datas = cursor.fetchall()
# for data_list in datas:
#     print(data_list)

# cursor.close()
# basic_data.close()