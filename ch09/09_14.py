import multiprocessing as mp
import websockets
import asyncio 
import json
import datetime
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import threading

async def korbit_ws_client(q):
    uri = "wss://ws.korbit.co.kr/v1/user/push"

    async with websockets.connect(uri) as websocket:
        now = datetime.datetime.now()
        timestamp = int(now.timestamp() * 1000)

        subscribe_fmt = {
            "accessToken": None, 
            "timestamp": timestamp, 
            "event": "korbit:subscribe",
            "data": {
                "channels": ["ticker:btc_krw"]
            }
        }
        subscribe_data = json.dumps(subscribe_fmt)
        await websocket.send(subscribe_data)

        while True:
            data = await websocket.recv()
            data = json.loads(data)
            q.put(data)

async def main(q):
    await korbit_ws_client(q)

def producer(q):
    proc = mp.current_process()
    print("producer's Process: ", proc.name)
    print("producer's Thread : ", threading.currentThread().getName())
    asyncio.run(main(q))

class Consumer(QThread):
    poped = pyqtSignal(dict)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        proc = mp.current_process()
        print("consumer's Process: ", proc.name)
        print("consumer's Thread : ", threading.currentThread().getName())

        while True:
            if not self.q.empty():
                data = q.get()
                self.poped.emit(data)


class MyWindow(QMainWindow):
    def __init__(self, q):
        super().__init__()
        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle("Korbit Websocket")

        # thread for data consumer
        proc = mp.current_process()
        print("windows's Process: ", proc.name)
        print("windows's Thread : ", threading.currentThread().getName())

        self.consumer = Consumer(q)
        self.consumer.poped.connect(self.print_data)
        self.consumer.start()

        # widget
        self.label = QLabel("Bitcoin: ", self)
        self.label.move(10, 10)

        # QLineEdit 
        self.line_edit = QLineEdit(" ", self)
        self.line_edit.resize(150, 30)
        self.line_edit.move(100, 10)

    @pyqtSlot(dict)
    def print_data(self, data):
        timestamp = data.get('timestamp')
        data_dict = data.get('data')
        last = data_dict.get('last')

        if last is not None:
            current_price = int(last)
            self.line_edit.setText(format(current_price, ",d"))

        now = datetime.datetime.fromtimestamp(int(timestamp)/1000)
        self.statusBar().showMessage(str(now))


if __name__ == "__main__":
    q = mp.Queue()
    p = mp.Process(name="Producer", target=producer, args=(q,), daemon=True)
    p.start()
    
    # Main process
    app = QApplication(sys.argv)
    mywindow = MyWindow(q)
    mywindow.show()
    app.exec_()