# -*- coding: utf-8 -*-
import os
import cv2
import numpy as np 
def different(img1, img2, difference_target = 90):
    #--- take the absolute difference of the images ---
    
    absolute = cv2.absdiff(img1, img2)

    #--- convert the result to integer type ---
    absolute = absolute.astype(np.uint8)

    #--- find percentage difference based on number of pixels that are not zero ---
    percentage = (np.count_nonzero(absolute) * 100)/ absolute.size

    print ("difference between images is %s%%" %(percentage))

    if percentage > difference_target:
        return True
    else:
        return False
        
    