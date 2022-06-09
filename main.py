import threading
import time
from src.capture import VideoCapture
from src.socks.client import SocketClient

# Socket client / Singleton
# server_host = '127.0.0.1'
# server_port = 4444
# socket = SocketClient(server_host, server_port)

video_cap = VideoCapture('examples/cars.mp4')
video_cap.execute()

# pList = []
# i = 0
# while(True):
#   pList.append(i)
#   if len(pList) >= 16:
#     pList.pop(0)
#   i = i + 1
#   print(pList)
#   time.sleep(.25)

# capture_thread = threading.Thread(target=video_cap.execute)
# capture_thread.start()
