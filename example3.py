
import cv2
import numpy as np


img = cv2.imread('testpic.jpg') 

img[50:200, 50:200] = (255,0,0)

cv2.imshow("test", img) #display of my modified image
cv2.waitKey(0) #display the image as long as I do not press a key
