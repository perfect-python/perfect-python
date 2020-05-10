#!/usr/bin/env python

"""
❶ ircライブラリーのインポート
"""
import irc.client

def on_connect(connection, event):
    """
    ❷ on_connectメソッドはIRCのネットワークに接続したときに呼び出されます。
    ここでは、#perfect_python_botというチャネルを検索して、
    チャネルが見つかれば接続します。
    """
    if irc.client.is_channel('#perfect_python_bot'):
        connection.join('#perfect_python_bot')
        return
    else:
        raise SystemExit(1)


def on_join(connection, event):
    """
    ❸ on_joinメソッドはチャネルに参加が完了したときに呼び出されます。
    """
    print("joined")

def on_pubmsg(connection, event):
    """
    ❹ on_pubmsgメッソッドはチャネル宛のメッセージを受信したときに呼び出されます。
    ここではメッセージがhelloのとき、チャネルにhiというメッセージを送ります。
    """
    if event.arguments[0] == "hello":
        sender = event.source.split("!")[0]
        connection.privmsg('#perfect_python_bot', "hi, " + sender )


def on_disconnect(connection, event):
    """
    ❺ on_disconnectメソッドは接続が切れたときに呼びされます。
    """
    raise SystemExit()


if __name__ == '__main__':
    """
    ❻　ircクライアントオブジェクトを作成して、reactor.server().connectでサーバの接続情報を作成します。
    """
    reactor = irc.client.Reactor()
    conn = reactor.server().connect('irc.friend-chat.jp', 6667, "PerfectPythonBot")

    """
    ❼　イベントハンドラーを設定します。ircプロトコルのコマンドに対応したイベントを指定します。
    """
    conn.add_global_handler("welcome", on_connect)
    conn.add_global_handler("join", on_join)
    conn.add_global_handler("pubmsg", on_pubmsg)
    conn.add_global_handler("disconnect", on_disconnect)

    """
    ❽　イベントループを回して処理を実行します。
    """
    reactor.process_forever()
