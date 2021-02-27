import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from pybithumb import Bithumb
# ----------------- 추 가 ------------------
import pybithumb
import datetime
import time
from PyQt5.QtCore import QThread, pyqtSignal

class VolatilityWorker(QThread):
    tradingSent = pyqtSignal(str, str, str)

    def __init__(self, ticker, bithumb):
        super().__init__()
        self.ticker = ticker
        self.bithumb = bithumb
        self.alive = True

    def run(self):
        while self.alive:
            self.tradingSent.emit("2021/03/04 12:11:41", "매수", "0.001")
            time.sleep(1)

    def close(self):
        self.alive = False
# ------------------------------------------

form_class = uic.loadUiType("resource/main.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ticker = "BTC"
        self.button.clicked.connect(self.clickBtn)

        with open("bithumb.txt") as f:
            lines = f.readlines()
            apikey = lines[0].strip()
            seckey = lines[1].strip()
            self.apiKey.setText(apikey)
            self.secKey.setText(seckey)

    def clickBtn(self):
        if self.button.text() == "매매시작":
            apiKey = self.apiKey.text()
            secKey = self.secKey.text()
            if len(apiKey) != 32 or len(secKey) != 32:
                self.textEdit.append("KEY가 올바르지 않습니다.")
                return
            else:
                self.bithumb = Bithumb(apiKey, secKey)
                self.balance = self.bithumb.get_balance(self.ticker)
                if self.balance == None:
                    self.textEdit.append("KEY가 올바르지 않습니다.")
                    return

            self.button.setText("매매중지")
            self.textEdit.append("------ START ------")
            self.textEdit.append(f"보유 코인 : {self.ticker} - {self.balance[0]} EA")
            # ----------------- 추 가 ------------------
            self.vw = VolatilityWorker(self.ticker, self.bithumb)
            self.vw.tradingSent.connect(self.ReceivetradingSignal)
            self.vw.start()
            # ------------------------------------------
        else:
            self.textEdit.append("------- END -------")
            self.button.setText("매매시작")

    # ----------------- 추 가 ------------------
    def ReceivetradingSignal(self, time, type, amount):
        self.textEdit.append(f"[{time}] {type} : {amount}")
    # ------------------------------------------

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    exit(app.exec_())
