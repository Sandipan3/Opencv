import cv2 as cv
import numpy as np

img=cv.imread("dog.jpg")
cv.imshow("img",img)

def translate(img, x,y):
    transmat=np.float32([[1,0,x],[0,1,y]])
    dim=(img.shape[1], img.shape[0] )
    return cv.warpAffine(img,transmat,dim)


translated=translate(img,100,100)
cv.imshow("translate",translated)

cv.waitKey(0)