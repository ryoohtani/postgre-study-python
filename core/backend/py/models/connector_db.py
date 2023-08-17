import psycopg2

class DbConnecotor(object):
    # DBの接続情報を定義
    def __init__(self, user, password, host, port, dbname):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.dbname = dbname
        # DB接続
        self.psyconnect = None
        # カーソルを作成してDB操作
        self.cursor = None

    # psycopg2を用いてDB接続を行う
    def pypost_connect(self):
        self.psyconnect = psycopg2.connect(
        user = self.user,
        password = self.password,
        host = self.host,
        port = self.port,
        dbname = self.dbname
        )
        self.cursor = self.psyconnect.cursor()