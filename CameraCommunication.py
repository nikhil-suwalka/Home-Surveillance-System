import socket
import threading
import time


class CameraCommunication:
    def __init__(self):
        self.s = socket.socket()
        self.port = 50001
        self.msg = ""

        # Get new port number
        try:
            while True:
                c = socket.socket()
                c.connect((socket.gethostname(), self.port))
                c.close()
                self.port += 1
        except Exception as e:
            pass

        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((socket.gethostname(), self.port))
        self.s.listen(5)

        accepter_thread = threading.Thread(target=self.clientAccepter)
        accepter_thread.start()

        heartbeat_thread = threading.Thread(target=self.heartbeat)
        heartbeat_thread.start()

    # for assigning new port numbers to new camera
    def clientAccepter(self):
        while True:
            c, addr = self.s.accept()
            c.close()

    # sends data to gui
    def heartbeat(self):
        gui = socket.socket()
        while True:
            try:
                string = str(self.port) + ": " + self.msg
                gui.send(string.encode())
            except:
                try:
                    gui.connect((socket.gethostname(), 50000))
                except:
                    pass
            time.sleep(2)

    def changeMessage(self, msg: str):
        self.msg = msg
