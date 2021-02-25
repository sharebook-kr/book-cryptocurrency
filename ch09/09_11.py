from pybithumb import WebSocketManager
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
import time


class Worker(QThread):
    recv = pyqtSignal(str)
    def run(self):
        # create websocket for Bithumb
        wm = WebSocketManager("ticker", ["BTC_KRW"])
        while True:
            data = wm.get()
            self.recv.emit(data['content']['closePrice'])


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        label = QLabel("BTC", self)
        label.move(20, 20)

        self.price = QLabel("-", self)
        self.price.move(80, 20)
        self.price.resize(100, 20)

        button = QPushButton("Start", self)
        button.move(20, 50)
        button.clicked.connect(self.click_btn)

        self.th = Worker()
        self.th.recv.connect(self.receive_msg)

    @pyqtSlot(str)
    def receive_msg(self, msg):
        print(msg)
        self.price.setText(msg)

    def click_btn(self):
       self.th.start()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   mywindow = MyWindow()
   mywindow.show()
   app.exec_()