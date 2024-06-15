import cv2 as cv
import numpy as np

img=cv.imread("dog.jpg")
cv.imshow("img", img)

blank=np.zeros(img.shape, dtype='uint8')

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

edge=cv.Canny(img,125,175)
cv.imshow("edge", edge)

contours,heirarchy=cv.findContours(edge,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

#blur image
#contours,heirarchy=cv.findContours(cv.GaussianBlur(edge,(3,3),cv.BORDER_DEFAULT),cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contour(s) found')

#visualize contour
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('draw',blank)

cv.waitKey(0)