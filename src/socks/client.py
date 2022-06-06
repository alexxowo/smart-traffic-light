import socket

class SocketClient:
  def __init__(self, host, port):
    print('Initializing Socket Client...')
    self.host = host
    self.port = port
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.sock.connect((self.host, self.port))

  def send(self, data):
    self.sock.send(data.encode())

  def close(self):
    self.sock.close()

