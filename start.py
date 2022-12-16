# -*- coding: utf-8 -*-
import time
import datetime
try :
    from universal_cap import universalCap
except:
    print("_____ERROR WHILE IMPORTING universalCap_____")

hour_start = 6
hour_stop = 22
while True:
    time_now= datetime.datetime.now()
    if time_now.hour > hour_start and time_now.hour < hour_stop:
        interval = 4
        difference_target = 76.1
        fps = 20
        x = 1280
        y = 720
        device = 0
        try: 
            universalCap(x,y,device,interval,difference_target, fps) #try capture with opencv 
        except:
            raise Exception ("_____universal camera error_____")
        print("\n")
    else:
        print("__________waiting for schedule__________")
        time.sleep(60)