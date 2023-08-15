import psycopg2

# 接続情報をどちらのbasic_dataを採用するか検討中
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

result = cursor.fetchone()
print(result[0] + "に接続完了")

# Pythonからpostgreへinsertする
cursor.execute("""insert into test_table(
               "ID", "売上日", "社員ID", "商品分類", "商品名", "単価", "数量", "売上金額") 
               values(
               300, '2023812', 'a003', '飲料', 'コーラ', 150, 200, 15000)""")

cursor.execute("""insert into test_table(
               "ID", "売上日", "社員ID", "商品分類", "商品名", "単価", "数量", "売上金額") 
               values
               (500, '2023815', 'a005', 'ゲーム機', '任天堂3DS', 15000, 600, 55000000)
""")

# update       
cursor.execute("""update test_table set "社員ID" = 'abcdef' where "社員ID" = 'a002'""")

# delete
cursor.execute("""delete from test_table where "社員ID" = 'a001'""")

# basic_data.commit()

# Pythonからpostgreへselect
cursor.execute("""select * from test_table""")
# cursor.execute("""select * from test_table where "社員ID" = 'a006'""")
datas = cursor.fetchall()
for data_list in datas:
    print(data_list)

cursor.close()
basic_data.close()


sqlalchemy