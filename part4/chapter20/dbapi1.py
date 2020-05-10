# ❶ インポート
import sqlite3

# ❷ メールアドレスのデータを格納するクラス
class MailAddress:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr

# ❸ データのインサート
def insert(conn, address):
    sql = "insert into mailaddress values (?, ?)"
    conn.execute(sql, (address.name, address.addr))

# ❹ データの取得
def select_all(conn):
    sql = "select * from mailaddress"
    cursor = conn.cursor()
    cursor.execute(sql)
    result = []
    for row in cursor:
        result.append(MailAddress(row[0], row[1]))
    return result

# ❺ 初期化
conn = sqlite3.connect(":memory:")
conn.execute("""
  create table mailaddress (
      name varchar(20),
      address varchar(64)
  );
  """)

# ❻ データの挿入と結果の取得
addr = MailAddress("Foo Bar", "foo@example.com")
insert(conn, addr)
result = select_all(conn)
for item in result:
    print(item.name + " : " + item.addr)

# ❼ 後始末
conn.close()
