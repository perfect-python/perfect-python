import sys
from PyQt5 import QtWebSockets, QtWidgets, Qt


def send_receive():
    ws = QtWebSockets.QWebSocket()

    def onstatechanged(state):
        if state == Qt.QAbstractSocket.ConnectedState:
            ws.sendTextMessage("Hello")

    def onreceived(data):
        print(data)
        QtWidgets.qApp.quit()

    ws.stateChanged.connect(onstatechanged)
    ws.textMessageReceived.connect(onreceived)
    ws.open(Qt.QUrl("ws://localhost:8080/ws"))


app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Send")
button.clicked.connect(send_receive)
button.show()
app.exec_()
