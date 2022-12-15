# -*- coding: utf-8 -*-
import cv2
import numpy as np 
def different(img1 = cv2.imread('C:\\Users\\usurio1\Downloads\\boardcapture-main\images\\test1.jpg', 0) , img2 = cv2.imread('C:\\Users\\usurio1\Downloads\\boardcapture-main\images\\test2.jpg', 0)):
    #img1 = cv2.imread('C:\\Users\\usurio1\Downloads\\boardcapture-main\images\\14-12-2022-19-25-34.png', 0)
    #img2 = cv2.imread('C:\\Users\\usurio1\Downloads\\boardcapture-main\images\\14-12-2022-19-29-43.png', 0)

    #--- take the absolute difference of the images ---
    absolute = cv2.absdiff(img1, img2)

    #--- convert the result to integer type ---
    absolute = absolute.astype(np.uint8)

    #--- find percentage difference based on number of pixels that are not zero ---
    percentage = (np.count_nonzero(absolute) * 100)/ absolute.size

    print (percentage)

different()