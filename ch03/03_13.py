import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)         

btn = QPushButton("Hello")    # 버튼 객체 생성
btn.show()

app.exec_()                   # 이벤트 루프 생성
