# -*- coding: utf-8 -*-
from picamera import PiCamera
import time
import datetime
capture_interval = 1
picamera = PiCamera()
picamera.resolution = (1280 ,720)
while True:
    time.sleep(capture_interval)
    picamera.capture(datetime.now().strftime("%Y-%m-%d-%H:%M:%S"))