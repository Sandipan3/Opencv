import cv2 as cv

img=cv.imread('dog.jpg')
cv.imshow('img',img)

med=cv.medianBlur(img,3)
cv.imshow('blur',med)

cv.waitKey(0)