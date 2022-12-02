# -*- coding: utf-8 -*-
from picamera import PiCamera

def image_cap(interval):

    
    camera = PiCamera()
    time.sleep(interval)

    camera.capture("/home/pi/Pictures/img.jpg")
    print("Done.")


