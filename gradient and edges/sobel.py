import cv2 as cv
import numpy as np

img=cv.imread('dog.jpg')
cv.imshow('img',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

x=cv.Sobel(gray,cv.CV_64F,1,0)
y=cv.Sobel(gray,cv.CV_64F,0,1)

cv.imshow('x',x)
cv.imshow('y',y)

combine=cv.bitwise_or(x,y)
cv.imshow('combine',combine)

cv.waitKey(0)