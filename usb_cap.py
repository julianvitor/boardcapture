# -*- coding: utf-8 -*-
import cv2
import time
import os

while True:
    webcam = cv2.VideoCapture(0)
    frame = webcam.read()[1]
    folder_path = str(os.getcwd()) + "\images"
    path = os.path.join(folder_path, "teste.png")
    # path = os.path.join("C:\Dev\\boardcapture\\fotos", "teste.png")
    time.sleep(1)

    cv2.imwrite(path, frame)
    print("capiturado")