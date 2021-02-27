from chart_widget import ChartWidget
from PyQt5.QtCore import QThread, pyqtSignal
from pybithumb import WebSocketManager

class PriceVolumeWorker(QThread):
    dataSent = pyqtSignal(int, float, float)

    def __init__(self, ticker):
        super().__init__()
        self.ticker = ticker
        self.alive = True

    def run(self):
        wm = WebSocketManager("ticker", [f"{self.ticker}_KRW"])
        while self.alive:
            data = wm.get()
            # ----------------- 수 정 ------------------
            date = int(data['content']['time'])
            price = float(data['content']['closePrice'])
            volume = float(data['content']['volume'])
            self.dataSent.emit(date, price, volume)
            # ------------------------------------------

    def stop(self):
        print('WTF')

    def close(self):
        self.alive = False


class ChartApp(ChartWidget):
    def __init__(self, ticker = "BTC"):
        super().__init__()
        self.pvw = PriceVolumeWorker(ticker)
        self.pvw.start()

    # ----------------- 추 가 ------------------
        self.pvw.dataSent.connect(self.receiveData)

    def receiveData(self, date, price, volume):
        print(date, price, volume)
        self.updateData(date, price, volume)
    # ------------------------------------------

    # def closeEvent(self, event):
    #     self.pvw.close()
    #     event.accept()


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    cca = ChartApp()
    cca.show()
    app.exec_()