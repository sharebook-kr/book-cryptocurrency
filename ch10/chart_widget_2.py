import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtChart import QLineSeries, QChart

class ChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("resource/chart.ui", self)

        self.priceData = QLineSeries()
        self.priceData.append(0, 10)
        self.priceData.append(1, 20)
        self.priceData.append(2, 10)

        self.priceChart = QChart()
        self.priceChart.addSeries(self.priceData)

        # ----------------- 추 가 ------------------
        self.priceChart.legend().hide()
        self.priceChart.createDefaultAxes()
        ax = self.priceChart.axisX(self.priceData)
        ax.setMin(0)
        ax.setMax(2)

        ay = self.priceChart.axisY(self.priceData)
        ay.setRange(0, 30)
        # ------------------------------------------

        self.priceView.setChart(self.priceChart)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    cw = ChartWidget()
    cw.show()
    exit(app.exec_())
