import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtChart import QLineSeries, QChart

class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("resource/chart.ui", self)

        self.priceData = QLineSeries()

        self.priceChart = QChart()
        self.priceChart.addSeries(self.priceData)
        self.priceChart.legend().hide()
        self.priceChart.createDefaultAxes()

        self.priceView.setChart(self.priceChart)


    def appendData(self, idx, price):
        self.priceData.append(idx, price)
        self.__updateAxis()


    def __updateAxis(self):
        ax = self.priceChart.axisX(self.priceData)
        ax.setMin(0)
        ax.setMax(2)

        ay = self.priceChart.axisY(self.priceData)
        ay.setRange(0, 30)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cw = ChartWidget()
    cw.appendData(0, 10)
    cw.appendData(1, 20)
    cw.appendData(2, 10)
    cw.show()
    exit(app.exec_())