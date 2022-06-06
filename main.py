import sched, time
from src.socks.client import SocketClient
from src.capture import VideoCapture

# video_cap = VideoCapture('examples/cars.mp4')
video_cap = VideoCapture(0)
# video_cap.execute();

while True:
  print('Count:' + str(video_cap.count_cars()))
  time.sleep(5)