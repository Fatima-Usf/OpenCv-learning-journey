import cv2
import numpy as np

#load the image
img = cv2.imread('testpic.jpg',0)

#Display the image
cv2.show("Hello openCv", img)


"""rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
