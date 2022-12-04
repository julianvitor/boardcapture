# -*- coding: utf-8 -*-
from picamera import PiCamera
import datetime
import time

def cls_capture(resolution_x=1920, resolution_y=1080, interval=10):

    try:
        camera = PiCamera()
        camera.resolution = (resolution_x, resolution_y)
        current_time = datetime.datetime.now()
        camera.capture("/home/pi/Pictures/%s-%s-%s:%s:%s:%s.png"%(current_time.day, current_time.month, current_time.year, current_time.hour, current_time.minute, current_time.second))
        print("capture completed at /home/pi/Pictures")
        time.sleep(interval)
    except:
        f = open("log.txt", "a")
        f.write("cls_camera_error")        
        f.close()
        print("_____CLS CAMERA ERROR_____")
        time.sleep(interval)

cls_capture()