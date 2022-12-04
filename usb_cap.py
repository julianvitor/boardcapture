# -*- coding: utf-8 -*-
import cv2
import time
import datetime
import os

while True:
    current_time = datetime.datetime.now()

    webcam = cv2.VideoCapture(0)
    frame = webcam.read()[0]
    
    if (webcam.isOpened()== False): 
        print("Error opening cam")

    folder_path = str(os.getcwd()) + "\images"
    file_name = "%s-%s-%s-%s-%s-%s.png"%(current_time.day, current_time.month, current_time.year, current_time.hour, current_time.minute, current_time.second)
    path = os.path.join(folder_path, file_name)
    print (path)
    # path = os.path.join("C:\Dev\\boardcapture\\fotos", "teste.png")
    
    time.sleep(3)

    cv2.imwrite(path, frame)
    print("capiturado em ", path)