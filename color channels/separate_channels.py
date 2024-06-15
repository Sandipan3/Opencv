import cv2 as cv
import numpy as np

img=cv.imread('dog.jpg')
cv.imshow('img',img)

blank=np.zeros(img.shape[:2],dtype='uint8')

b,g,r=cv.split(img)

blue=cv.merge([b,blank,blank])
cv.imshow('blue',blue)

green=cv.merge([blank,g,blank])
cv.imshow('green',green)

red=cv.merge([blank,blank,r])
cv.imshow('red',red)

cv.waitKey(0)