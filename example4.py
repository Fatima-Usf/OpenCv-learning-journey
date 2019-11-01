import cv2

""" we will draw geographic shapes and assign them colors"""

image = cv2.imread('testpic.jpg')
cropped = image[100:250, 200:350] #cropped take a part of our image

image[100:200, 100:200] = (255,0,0) 
image[300:350, 100:400] = (0,255,0)
image[400:500, 100:200] = (0,0,255)

cv2.imshow("test", image) 

cv2.imwrite('copy.jpg', image) # saving our image with the name "copy.jpg"
cv2.imwrite('cropped.jpg', cropped) 

cv2.waitKey(0) 