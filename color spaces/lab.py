import cv2 as cv

img=cv.imread("dog.jpg")
cv.imshow("img", img)

lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)

cv.waitKey(0)