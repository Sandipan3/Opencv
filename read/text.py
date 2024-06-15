import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')

cv.putText(blank,"hello", (0,255),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),thickness=1)
cv.imshow('blank', blank)

cv.waitKey(0)