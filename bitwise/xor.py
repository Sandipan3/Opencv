import cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype='uint8')

rectangle=cv.rectangle(blank.copy(), (30,30),(370,370),255,-1)
cv.imshow('rectangle',rectangle)

circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('circle',circle)

b_xor1=cv.bitwise_xor(rectangle,circle)
cv.imshow('xor',b_xor1)

cv.waitKey(0)