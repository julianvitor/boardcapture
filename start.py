# -*- coding: utf-8 -*-
import time
while True:
    try :
        from universal_cap import universalCap
    except:
        print("_____ERROR WHILE IMPORTING universalCap_____")
    try :
        from cls_cap import clsCapture
    except:
        print ("_____ERROR WHILE IMPORTING clsCapture_____")
        pass


    try: 
        universalCap(1920,1080,0) #try capture at secondary device 
    except:
        raise Exception ("_____universal camera error_____")

    try:
        clsCapture(1920,1080)
    except: 
        print ("_____cls camera error_____")
    time.sleep(3)
