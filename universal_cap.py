# -*- coding: utf-8 -*-
import cv2, datetime, os

def universalCap(heigth, width, device = 0, inside_folder_path = str(os.getcwd()) + "\images", fps = 60):
    current_time = datetime.datetime.now()

    camera = cv2.VideoCapture(device) #parameter for device set (0 is default)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, heigth)
    camera.set(cv2.CAP_PROP_FRAME_WIDTH, width )
    camera.set(cv2.CAP_PROP_FPS, fps)
    if (camera.isOpened()== False): 
        raise Exception ("_____ERROR WHILE OPENING CAMERA_____")

    ret,frame = camera.read()
    if (ret==False):
        raise Exception ("_____ERROR WHILE READING CAMERA DATA_____")


    #inside_folder_path = str(os.getcwd()) + "\images"
    try:

        file_name = "%s-%s-%s-%s-%s-%s.png"%(current_time.day, current_time.month, current_time.year, current_time.hour, current_time.minute, current_time.second)
        path = os.path.join(inside_folder_path, file_name)
        cv2.imwrite(path, frame)
        print("capiturado em ", path)

    except:
        raise Exception ("_____ERROR WHILE SAVING IMAGE AT STORAGE_____")


