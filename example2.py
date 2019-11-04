import cv2
import numpy as np

import cv2
# here M loading the image with its original colors 
image = cv2.imread('testpic.jpg')

height = image.shape[0] # the variable height takes the value of the height of our image
width = image.shape[1] # same for the width


print (height, width) 


#cv2.imshow("test", image)
cv2.imshow("test", flipVertical)

cv2.waitKey(2000)







"""rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
