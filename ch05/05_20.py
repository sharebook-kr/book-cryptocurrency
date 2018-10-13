import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import pybithumb

tickers = ["BTC", "ETH", "BCH", "ETC"]
form_class = uic.loadUiType("bull.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tableWidget.setRowCount(len(tickers))
        timer = QTimer(self)
        timer.start(5000)
        timer.timeout.connect(self.timeout)

    def timeout(self):
        try:
            for i, ticker in enumerate(tickers):
                ticker_item = QTableWidgetItem(ticker)
                self.tableWidget.setItem(i, 0, ticker_item)

                price, last_ma5, state = self.get_market_infos(ticker)
                self.tableWidget.setItem(i, 1, QTableWidgetItem(str(price)))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(str(last_ma5)))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(str(state)))
        except:
            pass

    def get_market_infos(self, ticker):
        try:
            df = pybithumb.get_ohlcv(ticker)
            ma5 = df['close'].rolling(window=5).mean()

            price = pybithumb.get_current_price(ticker)
            last_ma5 = ma5[-2]

            state = None
            if price > last_ma5:
                state = "상승장"
            else:
                state = "하락장"

            return (price, last_ma5, state)
        except:
            return (None, None, None)


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()