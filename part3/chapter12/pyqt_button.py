import sys
from PyQt5 import QtWidgets, Qt

app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Hello")
button.clicked.connect(Qt.qApp.quit)
button.show()
app.exec_()