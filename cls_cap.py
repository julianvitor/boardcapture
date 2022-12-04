# -*- coding: utf-8 -*-
from picamera import PiCamera #this module works just at unix systems, and is necessary a PI based hardware
import datetime
import os

def clsCapture(resolution_x=1920, resolution_y=1080,inside_folder = str(os.getcwd())+"\images_cls"):
    current_time = datetime.datetime.now()
    file_name = "%s-%s-%s-%s-%s-%s.png"%(current_time.day, current_time.month, current_time.year, current_time.hour, current_time.minute, current_time.second)
    full_file_path = os.path.join(inside_folder, file_name)
    try:
        camera = PiCamera()
        camera.resolution = (resolution_x, resolution_y)
        camera.capture(full_file_path)
        print("capture completed at %s"(str(inside_folder)))
    except:
        f = open("log.txt", "a")
        f.write("cls_camera_error"+"\n")        
        f.close()
        print("_____CLS CAMERA ERROR_____")



"""#coding -*- coding: utf-8 -*-
from picamera import PiCamera
import time
time.sleep(2)
camera = PiCamera()
camera.resolution = (1920, 1080)
camera.capture("/images/img.jpg")
print("captured at /images/img.jpg")

"""