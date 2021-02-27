import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

class OverviewWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("resource/overview.ui", self)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ob = OverviewWidget()
    ob.show()
    exit(app.exec_())
