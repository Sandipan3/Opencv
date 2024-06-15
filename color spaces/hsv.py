import cv2 as cv

img=cv.imread("dog.jpg")
cv.imshow("img", img)

hs=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hs)

cv.waitKey(0)