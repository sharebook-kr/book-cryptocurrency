import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtChart import QLineSeries, QChart, QValueAxis
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
        axisY0.setRange(0, 200)

        self.priceData = QLineSeries()
        self.priceChart = QChart()
        self.priceChart.addSeries(self.priceData)
        self.priceChart.legend().hide()

        self.priceChart.addAxis(axisX0, Qt.AlignBottom)
        self.priceChart.addAxis(axisY0, Qt.AlignRight)
        self.priceData.attachAxis(axisX0)
        self.priceData.attachAxis(axisY0)

        self.priceView.setChart(self.priceChart)
        self.dataLastIdx = 0

        # ----------------- 추 가 ------------------
        self.priceData.append(0, 10000)
        self.priceData.append(1, 12000)
        self.priceData.append(2, 8900)
        ay = self.priceChart.axisY()
        ay.setRange(40, 15000)
        ay.setTickInterval(1)
        # ------------------------------------------


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cw = ChartWidget()
    cw.show()
    exit(app.exec_())
