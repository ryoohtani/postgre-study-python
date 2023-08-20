import psycopg2

# 接続情報の記述パターンについては現在検討中(パターン1の可能性大)
# パターン1
basic_data = psycopg2.connect("postgresql://{user}:{password}@{host}:{port}/{dbname}".format(
    user = "admin",
    password = "pypost",
    host = "172.21.0.2",
    port = "5432",
    dbname = "test_database"))

# パターン2
# basic_data = psycopg2.connect(dbname = "test_database", host = "172.21.0.2", port = "5432", password = "pypost", user = "admin")

cursor = basic_data.cursor()

cursor.execute("select version();")
version = cursor.fetchone()
print(version[0] + "に接続完了")

# CREATE文
cursor.execute("""
                CREATE TABLE learning_table(
                EMPLOYEE_CODE varchar(10) NOT NULL,
                POSITION_NO varchar(5) NOT NULL,
                GENDER varchar(1),
                BASE_SALARY int,
                DATE_OF_HIRE date,
                PRIMARY KEY(EMPLOYEE_CODE))
               """)

# 以下コメントアウトはナレッジとして保管(1行ずつデータの挿入)
# cursor.execute("""
#                insert into learning_table(
#                EMPLOYEE_CODE, POSITION_NO, GENDER, BASE_SALARY, DATE_OF_HIRE
#                ) values ('s001', '1', '男', '200000', '2023-8-01')
#                """)

# cursor.execute("""
#                insert into learning_table(
#                EMPLOYEE_CODE, POSITION_NO, GENDER, BASE_SALARY, DATE_OF_HIRE
#                ) values ('s002', '2', '女', '210000', '2023-8-10')
#                """)

# cursor.execute("""
#                insert into learning_table(
#                EMPLOYEE_CODE, POSITION_NO, GENDER, BASE_SALARY, DATE_OF_HIRE
#                ) values ('s003', '3', '男', '220000', '2023-8-15')
#                """)

# cursor.execute("""
#                insert into learning_table(
#                EMPLOYEE_CODE, POSITION_NO, GENDER, BASE_SALARY, DATE_OF_HIRE
#                ) values ('s010', '4', '男', '22000', '2023-8-20')
#                """)

# Pythonからpostgresへinsert
cursor.execute("""
               insert into learning_table(
               EMPLOYEE_CODE, POSITION_NO, GENDER, BASE_SALARY, DATE_OF_HIRE
               ) values ('s001', '1', '男', '200000', '2023-8-01'),
               ('s002', '2', '女', '210000', '2023-8-10'),
               ('s003', '3', '男', '220000', '2023-8-15'),
               ('s010', '4', '男', '22000', '2023-8-20')
               """)

# update       
cursor.execute("""update learning_table set EMPLOYEE_CODE = 's004' where EMPLOYEE_CODE = 's010'""")

# delete
cursor.execute("""delete from learning_table where EMPLOYEE_CODE = 's004'""")

basic_data.commit()

# Pythonからpostgreへselect
cursor.execute("""select * from learning_table""")
datas = cursor.fetchall()
for data_list in datas:
    print(data_list)

cursor.execute("""select * from learning_table where gender = '男'""")
datas = cursor.fetchall()
for data_list in datas:
    print(data_list)

cursor.close()
basic_data.close()