import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
 
 
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)
 
    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)
 
 
app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()