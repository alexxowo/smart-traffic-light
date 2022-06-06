import cv2
import imutils
import numpy as np
from src.socks.client import SocketClient

class VideoCapture:
  def __init__(self, src=0):
    self.socket_client = SocketClient('127.0.0.1', 4444);
    self.cap = cv2.VideoCapture(src)
    self.classifier = cv2.CascadeClassifier('src/models/cars.xml')

  def send_socket_data(self, data):
    if data != '':
      self.socket_client.send(data)
      print('Data sent: ', data)

  def classifier_cars(self, frame):
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return self.classifier.detectMultiScale(grayscale_frame, 1.05, 5)

  def execute(self):
    while True:
      ret, frame = self.cap.read()

      resize_frame = imutils.resize(frame, width=780)
      vehicles_classifier = self.classifier_cars(resize_frame)

      for (x,y,w,h) in vehicles_classifier:
        cv2.rectangle(resize_frame, (x,y), (x+w,y+h), (255,150,0), 1)

      if ret is True:
        cv2.imshow('Video', resize_frame)

      if cv2.waitKey(120) & 0xFF == ord('q'):
        break

      self.send_socket_data(str(len(vehicles_classifier)))

    self.cap.release()
    self.socket_client.close()

  def count_cars(self) -> int:
    _, image_from_video = self.cap.read()
    resize_image = imutils.resize(image_from_video, width=780)
    vehicles = self.classifier_cars(resize_image)

    for (x,y,w,h) in vehicles:
      cv2.rectangle(resize_image, (x,y), (x+w,y+h), (255,150,0), 1)

    cv2.imshow('Capture', resize_image)

    return len(vehicles)



