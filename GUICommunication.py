import socket
import threading
import time


class GUICommunication:
    def __init__(self):
        self.s = socket.socket()
        self.port = 50000
        self.s.bind((socket.gethostname(), self.port))
        self.s.listen(5)
        self.cameras = []
        self.camera_messages = {}
        self.camera_status = {}

        camera_accepter_thread = threading.Thread(target=self.cameraAccepter)
        camera_accepter_thread.start()

    def listen(self, c: socket.socket, addr):
        while True:
            msg = str(c.recvmsg(1024)[0].decode())
            camera_port = msg.split(": ")[0]
            self.camera_messages[camera_port] = msg.split(": ")[1]
            self.camera_status[camera_port] = time.time()

    # Camera No : Online | Detected msg
    def getListOfMessages(self) -> list:
        result = []
        for port in self.camera_messages.keys():
            result.append(
                f"Camera {str(50000 - int(port))}: {'Online' if time.time() - self.camera_status[port] < 5 else 'Offline'} | {self.camera_messages[port]}")
        return result

    def cameraAccepter(self):
        while True:
            c, addr = self.s.accept()
            self.cameras.append((c, addr))
            receive_messages_thread = threading.Thread(target=self.listen, args=(c, addr))
            receive_messages_thread.start()
