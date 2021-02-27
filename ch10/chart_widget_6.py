import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtChart import QLineSeries, QChart, QBarSeries, QBarSet

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

        self.volumeData = QBarSeries()
        self.volumeChart = QChart()
        self.volumeChart.addSeries(self.volumeData)
        self.volumeChart.createDefaultAxes()
        self.volumeChart.legend().hide()
        self.volumeView.setChart(self.volumeChart)

        # ----------------- 추 가 ------------------
        volumeSet = QBarSet("data-0")
        volumeSet << 10 << 20 << 30
        self.volumeData.append(volumeSet)

        volumeSet = QBarSet("data-1")
        volumeSet << 30 << 20 << 10
        self.volumeData.append(volumeSet)
        # ------------------------------------------

        self.dataLimit = 60
        self.viewLimit = 30


    def updateData(self, idx, price):
        if len(self.priceData) == self.dataLimit :
            self.priceData.remove(0)
        self.priceData.append(idx, price)
        self.__updateAxis()


    def __updateAxis(self):
        minValX = sys.maxsize
        maxValX = 0
        minValY = sys.maxsize
        maxValY = 0
        for p in self.priceData.pointsVector()[-self.viewLimit:]:
            minValX = min(minValX, p.x())
            maxValX = max(maxValX, p.x())
            minValY = min(minValY, p.y())
            maxValY = max(maxValY, p.y())
        padding = (maxValY - minValY) / 10

        ax = self.priceChart.axisX(self.priceData)
        ax.setRange(minValX, maxValX)
        ay = self.priceChart.axisY(self.priceData)
        ay.setRange(minValY - padding, maxValY + padding)
        ay.setLabelFormat("%d")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cw = ChartWidget()
    for i in range(100):
        cw.updateData(i, i)
    cw.show()
    exit(app.exec_())
