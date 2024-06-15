import cv2 as cv
import numpy as np

img=cv.imread("dog.jpg")
cv.imshow("img",img)

flip=cv.flip(img,-1)
cv.imshow("flip",flip)

cv.waitKey(0)