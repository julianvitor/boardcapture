# -*- coding: utf-8 -*-
import cv2, datetime, os, glob, time
from diference_opencv import different

def universalCap(width = 1280 ,heigth = 720, device = 0,interval = 1,difference_target = 95, fps = 1, inside_folder = str(os.getcwd()) + "\images"):
    print("__________frame 1__________")
    try:
        camera = cv2.VideoCapture(device) #parameter for device set (0 is default)
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, width )
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, heigth)
        camera.set(cv2.CAP_PROP_FPS, fps)
    except:
        raise Exception ("_____ERROR WITH CAMERA SET/PROPERTIES_____")
    try:
        #print ("camera aberta", camera.isOpened())
        camera.isOpened()== True 
    
    except:
        raise Exception ("_____ERROR WHILE OPENING CAMERA_____")

    
    ret,frame = camera.read()
    current_time = datetime.datetime.now()
    time.sleep(interval)
    
    if (ret==False):
        raise Exception ("_____ERROR WHILE READING CAMERA DATA(check properties)_____")
    try:
        if not os.path.exists(str(os.getcwd()) + "\images"):
            os.makedirs(str(os.getcwd()) + "\images")
    except:
        raise Exception ("_____ERROR WHILE CREATING FOLDER FOR UNIVERSAL_____")
    
    
    try:

        file_name = "%s-%s-%s-%s-%s-%s.png"%(current_time.day, current_time.month, current_time.year, current_time.hour, current_time.minute, current_time.second)
        full_file_path = os.path.join(inside_folder, file_name)
        cv2.imwrite(full_file_path, frame)
        print("FRAME1 WRITE AT", full_file_path)

    except:
        raise Exception ("_____ERROR WHILE SAVING IMAGE AT STORAGE_____")
    
    
    
    



#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^frame1^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvframe2vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv
    
    print("__________frame 2__________")
    ret2,frame2 = camera.read()
    current_time2 = datetime.datetime.now()
    time.sleep(interval)
    
    
    if (ret2==False):
        raise Exception ("_____ERROR WHILE READING CAMERA DATA(check properties)_____")
    
    if different(frame, frame2, difference_target) == True:
        try:

            file_name = "%s-%s-%s-%s-%s-%s.png"%(current_time2.day, current_time2.month, current_time2.year, current_time2.hour, current_time2.minute, current_time2.second)
            full_file_path = os.path.join(inside_folder, file_name)
            cv2.imwrite(full_file_path, frame2)
            print("*DIFFERENT, WRITE AT ", full_file_path)
            

        except:
            raise Exception ("_____ERROR WHILE SAVING IMAGE AT STORAGE_____")

    else:
        print("*IMAGE SIMILAR, REMOVING%s"%(full_file_path))
        os.remove(full_file_path)
    
    

    
