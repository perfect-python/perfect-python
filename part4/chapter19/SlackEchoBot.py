import slack

# ❶受信するイベントを指定
@slack.RTMClient.run_on(event='message')
def echo(**payload):
    # ❷ボットクライアントのオブジェクトの取得
    web_client = payload['web_client']

    # ❸dataからメッセージに関する情報を取得
    data = payload['data']
    channel_id = data['channel']
    thread_ts = data['ts']
    user = data.get('user', None)
    message = data.get('text', [])
    

    if user and message:
        # ❹チャネルにメッセージを送信
        web_client.chat_postMessage(
            channel = channel_id,
            thread_ts = thread_ts,
            text = f"<@{user}> Re: {message}"
        )


slack_token = 'Slackのボット用トークン'
# ❹RTMのクライアントを作成して、イベントに応じて処理を実行
rtm_client = slack.RTMClient(token=slack_token)
rtm_client.start()
