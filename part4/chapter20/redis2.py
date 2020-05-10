import redis

client = redis.Redis(host='localhost', port=6379, db=0)
# ❶ クライアントオブジェクトの生成
pipe = client.pipeline()

d = {'id': 2012, 'email': 'foo@example.com', 'birthday': '2112/09/03'}
# ❷ pipeline にコマンドを溜めてから実行する
pipe = pipe.hmset('user:{id}'.format(**d), d).set('lookup:email:{email}'.format(**d), 
d['id'])
pipe.execute()
