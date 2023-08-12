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

# insert文修正中
cursor.execute("""insert into test_table ("ID", "売上日", "社員ID", "商品分類", "商品名", "単価", "数量", "売上金額") VALUES 
               ('500', '2023-8-12', 'a005', '飲料', 'コーラ', '150', '200', '15000')
""")

cursor.execute("select * from test_table")

row = cursor.fetchall()
for rows in row:
    print(rows)

cursor.close()
basic_data.close()