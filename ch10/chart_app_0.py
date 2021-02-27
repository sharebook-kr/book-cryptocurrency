from chart_widget import ChartWidget

class ChartApp(ChartWidget):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    cca = ChartApp()
    cca.show()
    app.exec_()