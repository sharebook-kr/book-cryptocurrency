import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtChart import QLineSeries, QChart, QBarSeries, QBarSet
from PyQt5.QtChart import QValueAxis
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt

class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("resource/chart.ui", self)

        self.dataLimit = 60
        self.viewLimit = 30

        axisX0 = QValueAxis()
        axisX0.setRange(0, self.viewLimit)
        axisX0.setVisible(False)
        axisY0 = QValueAxis()
        axisY0.setLabelFormat("%d")

        self.priceData = QLineSeries()
        self.priceChart = QChart()
        self.priceChart.addSeries(self.priceData)
        self.priceChart.legend().hide()

        margins = self.priceChart.margins()
        margins.setRight(margins.right() + 30)
        self.priceChart.setMargins(margins)

        # 반드시 chart에 axis 추가하고 series에 추가해야 함
        # - below: Qt::AlignBottom, left: Qt::AlignLeft, right: Qt::AlignRight, top: Qt::AlignTop
        self.priceChart.addAxis(axisX0, Qt.AlignBottom)
        self.priceChart.addAxis(axisY0, Qt.AlignRight)
        self.priceData.attachAxis(axisX0)
        self.priceData.attachAxis(axisY0)

        self.priceView.setChart(self.priceChart)
        self.dataLastIdx = 0


        # 봉차트




        self.volumeData = QBarSeries()
        self.volumeSet = QBarSet("volume")
        self.volumeData.append(self.volumeSet)
        self.volumeChart = QChart()
        self.volumeChart.addSeries(self.volumeData)
        self.volumeChart.legend().hide()
        self.volumeView.setChart(self.volumeChart)



        self.priceView.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.volumeView.setAttribute(Qt.WA_TransparentForMouseEvents)

        self.prevX = 0
        self.dataPos = 0


        self.priceData.append(0, 1000)
        self.priceData.append(1, 50)
        self.priceData.append(2, 80)
        ay = self.priceChart.axisY()
        ay.setRange(40, 1200)
        ay.setTickInterval(1)



    def mousePressEvent(self, e):
        self.prevX = e.x()


    def mouseReleaseEvent(self, e):
        currX = e.x()
        if currX > self.prevX :
            if self.dataPos >= 10:
                self.dataPos -= 10
        else:
            if self.dataPos < self.dataLimit - self.viewLimit - 1:
                self.dataPos += 10

        if len(self.priceData) != 0:
            self.__updateAxis()


    def updateData(self, idx, price, volume):
        if len(self.priceData) == self.dataLimit :
            self.priceData.remove(0)

        self.priceData.append(self.chartIdx, price)
        self.chartIdx += 1

        if len(self.volumeSet) == self.dataLimit :
            self.volumeSet.remove(0)
        self.volumeSet << (volume)
        self.__updateAxis()

        if len(self.priceData) == self.dataLimit:
            self.dataPos += 1


    def __updateAxis(self):
        minValX = sys.maxsize
        maxValX = 0
        minValY = sys.maxsize
        maxValY = 0

        for p in self.priceData.pointsVector()[self.dataPos : self.dataPos+self.viewLimit]:
            minValX = min(minValX, p.x())
            maxValX = max(maxValX, p.x())
            minValY = min(minValY, p.y())
            maxValY = max(maxValY, p.y())
        padding = (maxValY - minValY) / 10

        ax = self.priceChart.axisX(self.priceData)
        ax.setRange(minValX, maxValX)
        # ----------------- 추 가 ------------------
        ax.setVisible(False)
        # ------------------------------------------
        ay = self.priceChart.axisY(self.priceData)
        ay.setRange(minValY - padding, maxValY + padding)
        print(minValY, maxValY)
        ay.setLabelFormat("%d")

        self.volumeChart.createDefaultAxes()
        ax = self.volumeChart.axisX(self.volumeData)
        # ----------------- 추 가 ------------------
        ax.setVisible(False)
        # ------------------------------------------
        if len(self.volumeSet) > self.viewLimit:
            ax.setMin(ax.categories()[self.dataPos])
            lastIdx = min(len(self.volumeSet)-1, self.dataPos+self.viewLimit)
            ax.setMax(ax.categories()[lastIdx])
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
    import numpy as np

    # cw.updateData(125442, 54626000, 160.13317601)
    # cw.updateData(125446, 54640000, 160.07777601)
    # cw.updateData(125447, 54620000, 160.07887601)
    # cw.updateData(125449, 54620000, 160.08997601)

    # for i in range(100):
    #     cw.updateData(i, np.sin(i), i)
    cw.show()
    exit(app.exec_())
