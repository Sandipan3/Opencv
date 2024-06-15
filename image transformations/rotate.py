import cv2 as cv
import numpy as np

img=cv.imread("dog.jpg")
cv.imshow("img",img)

def rotate(img, angle,rotpoint=None):
    
    (height,width)=img.shape[:2]
    if rotpoint is None:
        rotpoint=(width//2,height//2)

    rotmat=cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dim=(width,height)
    return cv.warpAffine(img,rotmat,dim)

rotated=rotate(img,-45)
cv.imshow("rotate",rotated)

cv.waitKey(0)