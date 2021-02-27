import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("resource/chart.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cw = ChartWidget()
    cw.show()
    exit(app.exec_())
