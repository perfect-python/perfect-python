import redis

# ❶ クライアントオブジェクトの生成
client = redis.Redis(host='localhost', port=6379, db=0)

# ❷ リストの生成と追加
client.rpush('mylist', 'eggs')
client.rpush('mylist', 'ham')
client.lpush('mylist', 'spam')

# ❸ リストの取得
result = client.lrange('mylist', 0, -1)
print(result)

# ❹ リストから値の削除
client.lrem('mylist', 0, 'eggs')

# ❺ ハッシュの生成と値の設定
client.hset('words', 'jugem', 'goko')
print(client.hget('words', 'jugem'))

# ❻ Pythonの辞書を一気に登録
d = {'spam': 'salty', 'eggs': 'mild', 'ham': 'ioly'}
client.hmset('words', d)
print(client.hgetall('words'))
