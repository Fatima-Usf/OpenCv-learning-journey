import cv2
import numpy as np

#load the image
img = cv2.imread('testpic.jpg',0)

#Display the image and give it a name which is "hello opencv"
cv2.imshow("Hello openCv", img)

#Destroy the window after 1 sec
cv2.waitKey(2000)


"""rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
