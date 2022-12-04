#coding -*- coding: utf-8 -*-
from picamera import PiCamera
import time

time.sleep(2)
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.capture("/home/pi/Pictures/img.jpg")
print("Done.")

