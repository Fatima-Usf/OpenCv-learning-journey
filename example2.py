import cv2
import numpy as np

import cv2
#here M loading the image and keeping it original colors 
image = cv2.imread('testpic.jpg')

height = image.shape[0] # the variable height takes the value of the height of our image
width = image.shape[1] # same for the width


print (height, width) # print the height and the width


cv2.imshow("test", image) #display the image

cv2.waitKey(2000) #wait 2 sec





