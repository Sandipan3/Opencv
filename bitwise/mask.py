import cv2 as cv
import numpy as np

img=cv.imread('dog.jpg')
cv.imshow('img',img)

blank=np.zeros((img.shape[:2]),dtype='uint8')

circle=cv.circle(blank.copy(),(img.shape[1]//2 ,img.shape[1]//2 -100 ),200,255,-1)
cv.imshow('circle',circle)

mask=cv.bitwise_and(img,img,mask=circle)
cv.imshow('mask',mask)

cv.waitKey(0)