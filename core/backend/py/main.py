import psycopg2

conn = psycopg2.connect("postgresql://{user}:{password}@{host}:{port}/{dbname}".format(
    user = "admin",
    password = "pypost",
    host = "172.21.0.2",
    port = "5432",
    dbname = "test_database"))

cursor = conn.cursor()
cursor.execute("select version();")
result = cursor.fetchone()

print(result[0] + "に接続完了")

cursor.execute("select * from test_table")

row = cursor.fetchall()
for rows in row:
    print(rows)

cursor.close()
conn.close()