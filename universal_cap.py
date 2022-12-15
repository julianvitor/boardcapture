# -*- coding: utf-8 -*-
import cv2, datetime, os, time
from diference_opencv import different

#este primeiro grande bloco captura um frame e o grava em disco e mantem na memoria
def universalCap(width = 1920 ,heigth = 1280, device = 0,interval = 3, inside_folder = str(os.getcwd()) + "\images", fps = 60):
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
        print("escrito em", full_file_path)

    except:
        raise Exception ("_____ERROR WHILE SAVING IMAGE AT STORAGE_____")
    
    
    
    time.sleep(interval)

#este segundo frame é lido e armazenado na memoria para ser comparado com o primeiro frame

    ret2,frame2 = camera.read()
    
    if (ret2==False):
        raise Exception ("_____ERROR WHILE READING CAMERA DATA(check properties)_____")
    print("frame 2 try 3")
    try:
        if not os.path.exists(str(os.getcwd()) + "\images"):
            os.makedirs(str(os.getcwd()) + "\images")
    except:
        raise Exception ("_____ERROR WHILE CREATING FOLDER FOR UNIVERSAL_____")
    
    if different(frame, frame2) == True: # caso a diferença entre o anterior seja maior que um valor arbitrario o segundo frame sera salvo em disco
        current_time = datetime.datetime.now()
        print("frame 2 try 4")
        try:

            file_name = "%s-%s-%s-%s-%s-%s.png"%(current_time.day, current_time.month, current_time.year, current_time.hour, current_time.minute, current_time.second)
            full_file_path = os.path.join(inside_folder, file_name)
            cv2.imwrite(full_file_path, frame2)
            print("capiturado via opencv e gravado em", full_file_path)

        except:
            raise Exception ("_____ERROR WHILE SAVING IMAGE AT STORAGE_____")

    else:
        pass
#observação verificar logica para fora de pares, comparar imagem ja gravada com proxima imagem