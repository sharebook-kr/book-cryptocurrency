from chart_widget import ChartWidget
# ----------------- 추 가 ------------------
from PyQt5.QtCore import QThread, pyqtSignal
from pybithumb import WebSocketManager

class PriceVolumeWorker(QThread):
    dataSent = pyqtSignal(str, float, int)

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker

    def run(self):
        wm = WebSocketManager("ticker", [f"{self.ticker}_KRW"])
        while True:
            data = wm.get()
            print(data)
# ------------------------------------------

class ChartApp(ChartWidget):
    def __init__(self, ticker = "BTC"):
        super().__init__()
        # ----------------- 추 가 ------------------
        self.pvw = PriceVolumeWorker(ticker)
        self.pvw.start()
        # ------------------------------------------


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    cca = ChartApp()
    cca.show()
    app.exec_()