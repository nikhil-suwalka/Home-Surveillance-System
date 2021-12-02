import socket
import threading
import time


class CameraCommunication:
    def __init__(self):
        self.s = socket.socket()
        self.port = 50002
        self.msg = ""
        self.hostname = "192.168.196.172"
        # Get new port number
        try:
            while True:
                c = socket.socket()
                c.settimeout(0.5)
                c.connect((self.hostname, self.port))
                c.close()
                self.port += 1
        except Exception as e:
            print(e)

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
                    gui.connect((self.hostname, 50000))
                except Exception as e:
                    print(e)
            time.sleep(0.5)

    def changeMessage(self, msg: str):
        self.msg = msg
