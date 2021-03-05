import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from pybithumb import WebSocketManager

class OverViewWorker(QThread):
    # ----------------- 수 정 ------------------
    data24Sent = pyqtSignal(int, float, int, float, int, int)
    dataMidSent = pyqtSignal(int, float, float)
    # ------------------------------------------

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker
        self.alive = True

    def run(self):
        # ----------------- 수 정 ------------------
        wm = WebSocketManager("ticker", [f"{self.ticker}_KRW"], ["24H", "MID"])
        while self.alive:
            data = wm.get()

            if data['content']['tickType'] == "MID":
                self.dataMidSent.emit(int  (data['content']['closePrice'    ]),
                                      float(data['content']['chgRate'       ]),
                                      float(data['content']['volumePower'   ]))
            else:
                self.data24Sent.emit(int  (data['content']['closePrice'    ]),
                                     float(data['content']['volume'        ]),
                                     int  (data['content']['highPrice'     ]),
                                     float(data['content']['value'         ]),
                                     int  (data['content']['lowPrice'      ]),
                                     int  (data['content']['prevClosePrice']))
        # ------------------------------------------

        wm.terminate()

    def close(self):
        self.alive = False


class OverviewWidget(QWidget):
    def __init__(self, parent=None, ticker="BTC"):
        super().__init__(parent)
        uic.loadUi("resource/overview.ui", self)

        self.ticker = ticker
        self.ovw = OverViewWorker(ticker)
        # ----------------- 수 정 ------------------
        self.ovw.data24Sent.connect(self.fill24Data)
        self.ovw.dataMidSent.connect(self.fillMidData)
        # ------------------------------------------
        self.ovw.start()

    def closeEvent(self, event):
        self.ovw.close()

    # ----------------- 수 정 ------------------
    def fill24Data(self, currPrice, volume, highPrice, value, lowPrice, PrevClosePrice):
        self.label_1.setText(f"{currPrice:,}")
        self.label_4.setText(f"{volume:,.4f} {self.ticker}")
        self.label_6.setText(f"{highPrice:,}")
        self.label_8.setText(f"{value/100000000:,.1f} 억")
        self.label_10.setText(f"{lowPrice:,}")
        self.label_14.setText(f"{PrevClosePrice:,}")

    def fillMidData(self, currPrice, chgRate, volumePower):
        self.label_1.setText(f"{currPrice:,}")
        self.label_2.setText(f"{chgRate:+.2f}%")
        self.label_12.setText(f"{volumePower:.2f}%")
    # ------------------------------------------


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ob = OverviewWidget()
    ob.show()
    exit(app.exec_())
