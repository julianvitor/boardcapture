# -*- coding: utf-8 -*-
import cv2, datetime, os

def universalCap(width = 1920 ,heigth = 1280, device = 0, inside_folder = str(os.getcwd()) + "\images", fps = 60):
    print("try 1")

    try:
        camera = cv2.VideoCapture(device) #parameter for device set (0 is default)
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, width )
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, heigth)
        camera.set(cv2.CAP_PROP_FPS, fps)
    except:
        raise Exception ("_____ERROR WITH CAMERA SET/PROPERTIES_____")
    print("try 2")    
    try:
        #print ("camera aberta", camera.isOpened())
        camera.isOpened()== True 
       
    except:
        raise Exception ("_____ERROR WHILE OPENING CAMERA_____")

    ret,frame = camera.read()
    
    if (ret==False):
        raise Exception ("_____ERROR WHILE READING CAMERA DATA(check properties)_____")
    print("try 3")
    try:
        if not os.path.exists(str(os.getcwd()) + "\images"):
            os.makedirs(str(os.getcwd()) + "\images")
    except:
        raise Exception ("_____ERROR WHILE CREATING FOLDER FOR UNIVERSAL_____")
    
    current_time = datetime.datetime.now()
    print("try 4")
    try:

        file_name = "%s-%s-%s-%s-%s-%s.png"%(current_time.day, current_time.month, current_time.year, current_time.hour, current_time.minute, current_time.second)
        full_file_path = os.path.join(inside_folder, file_name)
        cv2.imwrite(full_file_path, frame)
        print("capiturado via opencv em", full_file_path)

    except:
        raise Exception ("_____ERROR WHILE SAVING IMAGE AT STORAGE_____")
universalCap()