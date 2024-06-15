import cv2 as cv
import numpy as np

img=cv.imread("dog.jpg")
cv.imshow("img",img)

crop=img[200:400, 200:400]
cv.imshow("crop",crop)

cv.waitKey(0)