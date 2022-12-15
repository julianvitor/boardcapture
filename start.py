# -*- coding: utf-8 -*-
import time
try :
    from universal_cap import universalCap
except:
    print("_____ERROR WHILE IMPORTING universalCap_____")
try :
    from cls_cap import clsCapture
except:
    print ("_____ERROR WHILE IMPORTING clsCapture_____")
    pass

while True:
    interval = 5
    try:
        clsCapture(1920,1080,0)#try capture with embedded camera
    except: 
        print ("_____cls camera error_____")
        try: 
            universalCap(1920,1080,0,interval) #try capture with opencv 
        except:
            raise Exception ("_____universal camera error_____")

    time.sleep(interval)
