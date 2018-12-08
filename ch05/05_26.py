from PyQt5.QtCore import *

class Worker(QThread):
    def run(self):
        while True:
            print("안녕하세요")
            self.sleep(1)