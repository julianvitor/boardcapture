# -*- coding: utf-8 -*-
from picamera import PiCamera
import datetime
import cv2

def cls_capture(resolution_x, resolution_y, interval):

    try:
        camera = PiCamera()
        camera.resolution = (resolution_x, resolution_y)
        time.sleep(interval)
        current_time = datetime.datetime.now()
        camera.capture("/home/pi/Pictures/%s-%s-%s:%s:%s:%s.png"%(current_time.day, current_time.month, current_time.year, current_time.hour, current_time.minute, current_time.second))
        print("capture completed at /home/pi/Pictures")
    except:
        f = open("log.txt", "a")
        f.write("cls_camera_error")        
        print("_____CLS CAMERA ERROR_____")

def usb_capture():
    cam_port = 0

