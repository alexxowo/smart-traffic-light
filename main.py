import threading
import time
from src.capture import VideoCapture

video_cap = VideoCapture('examples/cars2.mp4')
video_cap.execute()
