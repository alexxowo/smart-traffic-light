from numbers import Number
import time
from src.socks.client import SocketClient

socket_client = SocketClient('127.0.0.1', 4444)

while True:
  print(socket_client.receive())
  car_ratio = float(socket_client.receive())

  red_timing = car_ratio * 3.5
  green_timing = car_ratio * 5
  yellow_timing = 3

  print('Red timing:', red_timing, 'Green timing:', green_timing, 'Yellow timing:', yellow_timing)

  print('🟢')
  time.sleep(green_timing)
  print('🟠')
  time.sleep(yellow_timing)
  print('🔴')
  time.sleep(red_timing)