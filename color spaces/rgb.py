import cv2 as cv

img=cv.imread("dog.jpg")
cv.imshow("img", img)

rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)

cv.waitKey(0)