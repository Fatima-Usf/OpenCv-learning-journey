
import cv2
import numpy as np


img = cv2.imread('testpic.jpg') 

img[50:200, 50:200] = (255,0,0) # drew in the pixel from 50 to 200 with blue color

cv2.imshow("test", img) #display of my modified image
cv2.waitKey(0) #display the image as long as I do not press a key
