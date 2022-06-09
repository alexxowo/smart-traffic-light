import cv2
import imutils
from src.socks.server import SocketServer


class VideoCapture:
  def __init__(self, src=0):
    self.sock_server = SocketServer(4444)
    self.cap = cv2.VideoCapture(src)
    self.classifier = cv2.CascadeClassifier('src/models/cars.xml')
    self.car_ratio = 0.0
    self.lasted_cars = []

  def classifier_cars(self, frame):
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return self.classifier.detectMultiScale(grayscale_frame, 1.05, 6)

  def execute(self):
    while True:
      ret, frame = self.cap.read()

      resize_frame = imutils.resize(frame, width=780)
      vehicles_classifier = self.classifier_cars(resize_frame)

      self.lasted_cars.append(len(vehicles_classifier))
      if len(self.lasted_cars) >= 16:
        self.lasted_cars.pop(0)

      print('Cars:', self.lasted_cars, ' / Car ratio', round(sum(self.lasted_cars) / 15, 2), 'Veh/s')
      self.sock_server.send(str(round(sum(self.lasted_cars) / 15, 2)))

      for (x,y,w,h) in vehicles_classifier:
        cv2.rectangle(resize_frame, (x,y), (x+w,y+h), (255,150,0), 1)

      if ret is True:
        cv2.imshow('Video', resize_frame)

      if cv2.waitKey(500) & 0xFF == ord('q'):
        break

    self.cap.release()

  def count_cars(self) -> int:
    _, image_from_video = self.cap.read()
    resize_image = imutils.resize(image_from_video, width=780)
    vehicles = self.classifier_cars(resize_image)

    return resize_image, len(vehicles)
