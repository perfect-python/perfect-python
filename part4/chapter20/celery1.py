# ❶ mytaskからadd関数のインポート
from mytask import add
import time

# ❷ タスクの実行を依頼
delayed = add.delay(3,2)

# ❸ タスクの処理の終了を待つ
while delayed.ready() == False:
    time.sleep(1)

# ❹ 実行結果の出力
print(delayed.get())
