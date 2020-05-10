# ❶ Celeryのインポート
from celery import Celery

# ❷ Celeryオブジェクトの初期化
celery = Celery('mytasks',
                 backend='rpc://',
                 broker='amqp://localhost//'
)

# ❸ タスクの実装
@celery.task
def add(x, y):
    return x + y
