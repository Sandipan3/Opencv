import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
blank[200:300, 300:400]=0,255,0
cv.imshow('blank', blank)

cv.waitKey(0)