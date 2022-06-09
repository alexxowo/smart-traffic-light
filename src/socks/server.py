import socket

class SocketServer:
  def __init__(self, port):
    self.host = '127.0.0.1'
    self.port = port
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Initializing Socket Server...')
    print(('Host:', self.host, 'Port:', self.port))
    self.sock.bind((self.host, self.port))
    self.sock.listen(1)
    self.conn, self.addr = self.sock.accept()
    print('Connected to', self.addr)


  def send(self, data):
    self.conn.send(data.encode())

  def close(self):
    self.conn.close()

