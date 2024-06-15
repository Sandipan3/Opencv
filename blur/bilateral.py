import cv2 as cv

img=cv.imread('dog.jpg')
cv.imshow('img',img)

bilat=cv.bilateralFilter(img,5,15,15)
cv.imshow('bilateral_blur',bilat)

cv.waitKey(0)