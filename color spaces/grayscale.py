import cv2 as cv

img=cv.imread("dog.jpg")
cv.imshow("img", img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

cv.waitKey(0)