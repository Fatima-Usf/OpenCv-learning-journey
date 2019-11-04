import cv2
import imutils

""" Images Transformation """
image = cv2.imread('testpic.jpg')

rotated = imutils.rotate(image, 90) #Image rotation
resized = imutils.resize(image, width = 300) #We defne here a new size to our image
translated = imutils.translate(image,100,0) #décalage de l'image


cv2.imwrite('rotated.jpg', rotated) 
cv2.imshow('rotation', image)
cv2.waitKey(0)

cv2.imwrite('resized.jpg', resized) 
cv2.imwrite('translated.jpg', translated) 