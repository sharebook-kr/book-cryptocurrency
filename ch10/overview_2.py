import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from pybithumb import WebSocketManager

class OverViewWorker(QThread):
    dataSent = pyqtSignal(int, float, float, int, float, int, float, int)

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker
        self.alive = True

    def run(self):
        wm = WebSocketManager("ticker", [f"{self.ticker}_KRW"], ["24H"])
        while self.alive:
            data = wm.get()
            self.dataSent.emit(int  (data['content']['closePrice'    ]),
                               float(data['content']['chgRate'       ]),
                               float(data['content']['volume'        ]),
                               int  (data['content']['highPrice'     ]),
                               float(data['content']['value'         ]),
                               int  (data['content']['lowPrice'      ]),
                               float(data['content']['volumePower'   ]),
                               int  (data['content']['prevClosePrice']))
    # ----------------- 추 가 ------------------
        wm.terminate()

    def close(self):
        self.alive = False
    # ------------------------------------------


class OverviewWidget(QWidget):
    def __init__(self, parent=None, ticker="BTC"):
        super().__init__(parent)
        uic.loadUi("resource/overview.ui", self)

        self.ticker = ticker
        self.ovw = OverViewWorker(ticker)
        self.ovw.dataSent.connect(self.fillData)
        self.ovw.start()

    # ----------------- 추 가 ------------------
    def closeEvent(self, event):
        self.ovw.close()
     # ------------------------------------------

    def fillData(self, currPrice, chgRate, volume, highPrice, value, lowPrice, volumePower, PrevClosePrice):
        self.label_1.setText(f"{currPrice:,}")
        self.label_2.setText(f"{chgRate:+.2f}%")
        self.label_4.setText(f"{volume:,.4f} {self.ticker}")
        self.label_6.setText(f"{highPrice:,}")
        self.label_8.setText(f"{value/100000000:,.1f} 억")
        self.label_10.setText(f"{lowPrice:,}")
        self.label_12.setText(f"{volumePower:.2f}%")
        self.label_14.setText(f"{PrevClosePrice:,}")


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ob = OverviewWidget()
    ob.show()
    exit(app.exec_())
