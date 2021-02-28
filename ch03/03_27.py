import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MySignal(QObject):
    signal1 = pyqtSignal()

    def run(self):
        self.signal1.emit()


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        mysignal = MySignal()
        mysignal.signal1.connect(self.signal1_emitted)
        mysignal.run()

    @pyqtSlot()
    def signal1_emitted(self):
        print("signal1 emitted")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()