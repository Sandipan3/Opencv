import cv2 as cv

img=cv.imread('dog.jpg')
cv.imshow('img',img)

avg=cv.blur(img,(3,3))
cv.imshow('blur',avg)

cv.waitKey(0)