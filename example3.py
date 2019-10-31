
import cv2
import numpy as np


img = cv2.imread('testpic.jpg') 

img[50:200, 50:200] = (255,0,0)

cv2.imshow("test", img) #affichage de mon image modifiee
cv2.waitKey(0) # affichage de l'image tant que je n'appuie pas sur une touche
