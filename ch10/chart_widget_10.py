import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtChart import QLineSeries, QChart, QBarSeries, QBarSet
from PyQt5.QtCore import Qt

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
        self.volumeSet = QBarSet("volume")
        self.volumeData.append(self.volumeSet)
        self.volumeChart = QChart()
        self.volumeChart.addSeries(self.volumeData)
        self.volumeChart.legend().hide()
        self.volumeView.setChart(self.volumeChart)

        self.dataLimit = 60
        self.viewLimit = 30

        self.priceView.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.volumeView.setAttribute(Qt.WA_TransparentForMouseEvents)

        # ----------------- 추 가 ------------------
        self.prevX = 0
        self.dataPos = self.dataLimit - self.viewLimit - 1
        # ------------------------------------------

    def mousePressEvent(self, e):
        # ----------------- 수 정 ------------------
        self.prevX = e.x()
        # ------------------------------------------

    def mouseReleaseEvent(self, e):
        # ----------------- 수 정 ------------------
        currX = e.x()
        if currX > self.prevX :
            if self.dataPos >= 10:
                self.dataPos -= 10
        else:
            if self.dataPos < self.dataLimit - self.viewLimit - 1:
                self.dataPos += 10

        if len(self.priceData) != 0:
            self.__updateAxis()
        # ------------------------------------------


    def updateData(self, idx, price, volume):
        if len(self.priceData) == self.dataLimit :
            self.priceData.remove(0)
        self.priceData.append(idx, price)

        if len(self.volumeSet) == self.dataLimit :
            self.volumeSet.remove(0)
        self.volumeSet << (volume)
        self.__updateAxis()


    def __updateAxis(self):
        minValX = sys.maxsize
        maxValX = 0
        minValY = sys.maxsize
        maxValY = 0
        # ----------------- 수 정 ------------------
        for p in self.priceData.pointsVector()[self.dataPos : self.dataPos+self.viewLimit]:
        # ------------------------------------------
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

        self.volumeChart.createDefaultAxes()
        ax = self.volumeChart.axisX(self.volumeData)
        if len(self.volumeSet) > self.viewLimit:
            # ----------------- 수 정 ------------------
            ax.setMin(ax.categories()[self.dataPos])
            lastIdx = min(len(self.volumeSet)-1, self.dataPos+self.viewLimit)
            ax.setMax(ax.categories()[lastIdx])
            # ------------------------------------------
        else :
            ax.setMin(ax.categories()[0])

        ay = self.volumeChart.axisY(self.volumeData)
        minValY = min(self.volumeSet)
        maxValY = max(self.volumeSet)
        padding = (maxValY - minValY) / 10
        ay.setRange(max(0, minValY - padding), maxValY + padding)
        ay.setLabelFormat("%d")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cw = ChartWidget()
    # ----------------- 수 정 ------------------
    import numpy as np
    for i in range(100):
        cw.updateData(i, np.sin(i), i)
    # ------------------------------------------
    cw.show()
    exit(app.exec_())
