import cv2 as cv
import numpy as np

img=cv.imread("dog.jpg")
cv.imshow("img",img)

resize=cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow("resize", resize)

cv.waitKey(0)