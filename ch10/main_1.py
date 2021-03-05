import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("resource/main.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Home Trading System")

    # ----------------- 추 가 ------------------
        self.button.clicked.connect(self.clickBtn)

    def clickBtn(self):
        if self.button.text() == "매매시작":
            text = "매매중지"
        else:
            text = "매매시작"
        self.button.setText(text)
    # ------------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    exit(app.exec_())
