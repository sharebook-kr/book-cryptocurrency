from chart_widget import ChartWidget

class ChartApp(ChartWidget):
    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    cca = ChartApp()
    cca.setWindowTitle('Candlestic Charts')
    cca.show()
    app.exec_()

# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5 import uic
# from chart_widget_8 import ChartWidget

# class MyWindow(QMainWindow):
#        def __init__(self):
#         super().__init__()
#         uic.loadUi("resource/test.ui", self)
#         self.widget = ChartWidget(self)

#         for i in range(100):
#             self.widget.updateData(i, i, i)




# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWindow = MyWindow()
#     myWindow.show()
#     app.exec_()