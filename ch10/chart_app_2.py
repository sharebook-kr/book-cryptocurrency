from chart_widget import ChartWidget
from PyQt5.QtCore import QThread, pyqtSignal
from pybithumb import WebSocketManager

class PriceVolumeWorker(QThread):
    dataSent = pyqtSignal(str, float, int)

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker
        # ----------------- 추 가 ------------------
        self.alive = True
        # ------------------------------------------

    def run(self):
        wm = WebSocketManager("ticker", [f"{self.ticker}_KRW"])
        # ----------------- 수 정 ------------------
        while self.alive:
        # ------------------------------------------
            data = wm.get()
            print(data)

    # ----------------- 추 가 ------------------
    def close(self):
        self.alive = False
    # ------------------------------------------


class ChartApp(ChartWidget):
    def __init__(self, ticker = "BTC"):
        super().__init__()
        self.pvw = PriceVolumeWorker(ticker)
        self.pvw.start()

    def closeEvent(self, event):
        # ----------------- 추 가 ------------------
        self.pvw.close()
        event.accept()
        # ------------------------------------------


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    cca = ChartApp()
    cca.show()
    app.exec_()